// syndrome_calc.v -- integer syndrome calculator for a 14x48 Sidon parity matrix.
//
// lanes: 48 lanes x 2 bits, signed spike value per lane
//        (2'b01 = +1, 2'b00 = 0, 2'b11 = -1; 2'b10 never driven).
// syn:   14 components x 3 bits two's complement, component r at bits [3*r +: 3],
//        syn_r = sum_i lane_i * H[r][i]  over the integers (range -3..3 for
//        weight <= 3 fault patterns).
// COLS:  48 columns x 14 bits packed, column i at bits [14*i +: 14], bit r = H[r][i].
module syndrome_calc #(
    parameter [48*14-1:0] COLS = {48*14{1'b0}}
) (
    input  wire [48*2-1:0] lanes,
    output reg  [14*3-1:0] syn
);
    integer i, r;
    reg [47:0] colbits;      // column bits for the current row
    reg [47:0] pos_m, neg_m; // lanes at +1 / -1 masked by the row's column bits
    reg [5:0]  pc, nc;       // popcounts (0..48)
    reg signed [6:0] acc;

    always @* begin
        for (r = 0; r < 14; r = r + 1) begin
            for (i = 0; i < 48; i = i + 1)
                colbits[i] = COLS[14*i + r];
            for (i = 0; i < 48; i = i + 1) begin
                pos_m[i] = colbits[i] & (lanes[2*i +: 2] == 2'b01);
                neg_m[i] = colbits[i] & (lanes[2*i +: 2] == 2'b11);
            end
            pc = 0; nc = 0;
            for (i = 0; i < 48; i = i + 1) begin
                pc = pc + pos_m[i];
                nc = nc + neg_m[i];
            end
            acc = $signed({1'b0, pc}) - $signed({1'b0, nc});
            syn[3*r +: 3] = acc[2:0];
        end
    end
endmodule
