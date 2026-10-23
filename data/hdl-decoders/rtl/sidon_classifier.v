// sidon_classifier.v -- repair-or-refuse syndrome classifier (14x48 Sidon matrix).
//
// Classification (the verified level100 / v3-spec decoder semantics):
//   syn == 0           -> CLEAN  (class 0)
//   syn == +c_i / -c_i -> REPAIR (class 1, index = column i, sign)
//   syn == +e_r / -e_r -> TAIL   (class 2, index = row r, sign) [tail edit]
//   otherwise          -> REFUSE (class 3)
// All 48 column matches, both signs, and all 14 axis matches, both signs, are
// evaluated in parallel; disjointness for every weight <= 3 pattern is the
// verified Sidon refusal property, so the priority order below never actually
// arbitrates a conflict.
module sidon_classifier #(
    parameter [48*14-1:0] COLS = {48*14{1'b0}}
) (
    input  wire [14*3-1:0] syn,
    output reg  [1:0]      cls,     // 0 CLEAN, 1 REPAIR, 2 TAIL, 3 REFUSE
    output reg  [5:0]      index,   // column (REPAIR) or row (TAIL)
    output reg             sign     // 1 = positive, 0 = negative
);
    // expected packed syndrome for +column i (sign=1) or -column i (sign=0)
    function [14*3-1:0] exp_col;
        input integer i;
        input sign;
        integer r;
        begin
            for (r = 0; r < 14; r = r + 1)
                exp_col[3*r +: 3] = COLS[14*i + r] ?
                    (sign ? 3'sd1 : -3'sd1) : 3'sd0;
        end
    endfunction
    // expected packed syndrome for +axis row (sign=1) or -axis row (sign=0)
    function [14*3-1:0] exp_axis;
        input integer row;
        input sign;
        integer r;
        begin
            for (r = 0; r < 14; r = r + 1)
                exp_axis[3*r +: 3] = (r == row) ?
                    (sign ? 3'sd1 : -3'sd1) : 3'sd0;
        end
    endfunction

    wire [47:0] mp, mm;
    wire [13:0] ap, am;
    genvar gi, gr;
    generate
        for (gi = 0; gi < 48; gi = gi + 1) begin : gcol
            assign mp[gi] = (syn == exp_col(gi, 1'b1));
            assign mm[gi] = (syn == exp_col(gi, 1'b0));
        end
        for (gr = 0; gr < 14; gr = gr + 1) begin : gaxis
            assign ap[gr] = (syn == exp_axis(gr, 1'b1));
            assign am[gr] = (syn == exp_axis(gr, 1'b0));
        end
    endgenerate

    integer k;
    always @* begin
        cls = 2'd3; index = 6'd0; sign = 1'b0;
        if (syn == {14*3{1'b0}}) begin
            cls = 2'd0;
        end else if (|mp || |mm) begin
            cls = 2'd1;
            for (k = 0; k < 48; k = k + 1) begin
                if (mp[k]) begin index = k[5:0]; sign = 1'b1; end
                if (mm[k]) begin index = k[5:0]; sign = 1'b0; end
            end
        end else if (|ap || |am) begin
            cls = 2'd2;
            for (k = 0; k < 14; k = k + 1) begin
                if (ap[k]) begin index = k[5:0]; sign = 1'b1; end
                if (am[k]) begin index = k[5:0]; sign = 1'b0; end
            end
        end
    end
endmodule
