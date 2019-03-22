# PUF_ECE268_UCSD
Intrinsic PUF from machine learning models

## Setup

1. Download Vivado 2017.4 first to open the zip file.
2. Extract the puf_final zip file.
3. Open the Vivado project inside puf_final using the .xpr file present in extracted folder.
4. Add the Coarse_Tune.v, Decoder.v, PDL_coarse.v, PUF.v, PUF_unit.v present in the code.zip folder in the source files. 
5. The PUF_final_wrapper block design contain the custom IP generated by puf_final design and the AXI interface block generated through Vivado HLS.
6. We have already have the .bit file present in Vivado folder inside puf_final/puf_final/puf_final.runs/impl_1/PUF_final_wrapper.bit and puf_final/puf_final/puf_final.runs/impl_1/PUF_final_wrapper.tcl
7. Add the two files in the jupyter-notebooks folder to be used in as overlay to be run.
8.