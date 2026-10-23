// tb_decoder.v -- exhaustive testbench for the V4 Sidon decoders.
// Select the DUT with -DF64 or -DGF128. Drives every signed weight<=3 pattern
// (143,005 vectors incl. zero) through lanes -> syndrome_calc -> classifier,
// then every tail (axis) syndrome directly into a standalone classifier.
// Expected classes come from the Python golden model (gen_vectors.py).
`timescale 1ns/1ps
`ifdef F64
  `include "f64_cols.vh"
  `define COLS_MACRO `F64_COLS
  `define VECFILE "vectors/f64_vectors.hex"
  `define TAILFILE "vectors/f64_vectors_tails.hex"
`else
  `include "gf128_cols.vh"
  `define COLS_MACRO `GF128_COLS
  `define VECFILE "vectors/gf128_vectors.hex"
  `define TAILFILE "vectors/gf128_vectors_tails.hex"
`endif

module tb_decoder;
    reg  [48*2-1:0] lanes;
    wire [1:0] cls; wire [5:0] index; wire sign;

`ifdef F64
    decoder_f64 dut (.lanes(lanes), .cls(cls), .index(index), .sign(sign));
`else
    decoder_gf128 dut (.lanes(lanes), .cls(cls), .index(index), .sign(sign));
`endif

    // standalone classifier for the tail (axis) tests
    reg  [14*3-1:0] syn_t;
    wire [1:0] cls_t; wire [5:0] index_t; wire sign_t;
    sidon_classifier #(.COLS(`COLS_MACRO)) u_cls_t
        (.syn(syn_t), .cls(cls_t), .index(index_t), .sign(sign_t));

    integer fd, code, errors, checked, k;
    reg [20:0] pat;
    reg [8:0]  expv;
    reg [5:0]  sidx; reg ssgn;
    integer trow, tsgn;
    reg [8:0] texpv;

    initial begin
        errors = 0; checked = 0;
        // ---- pattern vectors through the full decoder ----
        fd = $fopen(`VECFILE, "r");
        if (fd == 0) begin $display("FAIL: cannot open vector file"); $finish; end
        while (!$feof(fd)) begin
            code = $fscanf(fd, "%h %h\n", pat, expv);
            if (code == 2) begin
                lanes = {48*2{1'b0}};
                for (k = 0; k < 3; k = k + 1) begin
                    sidx = pat[7*k +: 6];
                    ssgn = pat[7*k + 6];
                    if (sidx != 6'd63)
                        lanes[2*sidx +: 2] = ssgn ? 2'b01 : 2'b11;
                end
                #1;
                checked = checked + 1;
                if (cls !== expv[8:7]) begin
                    errors = errors + 1;
                    if (errors <= 10)
                        $display("MISMATCH pat=%h exp_cls=%0d got_cls=%0d", pat, expv[8:7], cls);
                end else if (expv[8:7] == 2'd1) begin
                    if (index !== expv[6:1] || sign !== expv[0]) begin
                        errors = errors + 1;
                        if (errors <= 10)
                            $display("REPAIR FIELD MISMATCH pat=%h exp idx=%0d sgn=%0d got idx=%0d sgn=%0d",
                                     pat, expv[6:1], expv[0], index, sign);
                    end
                end
            end
        end
        $fclose(fd);
        $display("patterns: %0d checked, %0d errors", checked, errors);
        // ---- tail vectors directly into the classifier ----
        checked = 0;
        fd = $fopen(`TAILFILE, "r");
        if (fd == 0) begin $display("FAIL: cannot open tails file"); $finish; end
        while (!$feof(fd)) begin
            code = $fscanf(fd, "%h %h %h\n", trow, tsgn, texpv);
            if (code == 3) begin
                syn_t = {14*3{1'b0}};
                syn_t[3*trow +: 3] = tsgn ? 3'sd1 : -3'sd1;
                #1;
                checked = checked + 1;
                if (cls_t !== texpv[8:7] || index_t !== texpv[6:1] || sign_t !== texpv[0]) begin
                    errors = errors + 1;
                    $display("TAIL MISMATCH row=%0d sgn=%0d exp=%h got cls=%0d idx=%0d sgn=%0d",
                             trow, tsgn, texpv, cls_t, index_t, sign_t);
                end
            end
        end
        $fclose(fd);
        $display("tails: %0d checked, %0d total errors", checked, errors);
        if (errors == 0) $display("TB RESULT: PASS");
        else             $display("TB RESULT: FAIL (%0d errors)", errors);
        $finish;
    end
endmodule
