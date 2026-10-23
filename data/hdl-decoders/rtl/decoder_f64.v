// decoder_f64.v -- V4 Sidon decoder, F_64 spec set (CONSOLIDATED DRAFT v3 SS3.5,
// construct_v4b.py MASKS4, poly 0x43, two common bits). Combinational:
// one syndrome classified per evaluation; register the I/O for 1/cycle throughput.
`include "f64_cols.vh"
module decoder_f64 (
    input  wire [48*2-1:0] lanes,
    output wire [1:0]      cls,
    output wire [5:0]      index,
    output wire            sign
);
    wire [14*3-1:0] syn;
    syndrome_calc    #(.COLS(`F64_COLS)) u_calc (.lanes(lanes), .syn(syn));
    sidon_classifier #(.COLS(`F64_COLS)) u_cls  (.syn(syn), .cls(cls), .index(index), .sign(sign));
endmodule
