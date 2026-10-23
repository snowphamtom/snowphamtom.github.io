// decoder_gf128.v -- V4 Sidon decoder, GF(2^7) fully-closed reserve-swapped set
// (seed6 with columns 8, 12, 16, 28, 36 swapped to reserve curve points;
// 69,184/69,184 distinct triple syndromes, verified 2026-10-22). Combinational.
`include "gf128_cols.vh"
module decoder_gf128 (
    input  wire [48*2-1:0] lanes,
    output wire [1:0]      cls,
    output wire [5:0]      index,
    output wire            sign
);
    wire [14*3-1:0] syn;
    syndrome_calc    #(.COLS(`GF128_COLS)) u_calc (.lanes(lanes), .syn(syn));
    sidon_classifier #(.COLS(`GF128_COLS)) u_cls  (.syn(syn), .cls(cls), .index(index), .sign(sign));
endmodule
