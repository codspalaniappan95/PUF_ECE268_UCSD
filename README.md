# PUF_ECE268_UCSD
Intrinsic PUF from machine learning models

## Setup

1. Download Vivado 2017.4 first to open the zip file.
2. Extract the puf_final zip file.
3. Open the Vivado project inside puf_final using the .xpr file present in extracted folder.
4. Add the Coarse_Tune.v, Decoder.v, PDL_coarse.v, PUF.v, PUF_unit.v present in the code.zip folder in the source files.
5. The PUF_final_wrapper block design contain the custom IP generated by puf_final design and the AXI interface block generated through Vivado HLS.
6. We have already have the .bit file present in Vivado folder inside puf_final/puf_final/puf_final.runs/impl_1/PUF_final_wrapper.bit and puf_final/puf_final/puf_final.runs/impl_1/PUF_final_wrapper.tcl.
7. Add the two files in the jupyter-notebooks folder to be used in as overlay to be run.
8. Use the PUF.ipynb and copy it inside the jupyter-notebooks folder in in the PYNQ hierarchy.
9. You can observe the constraints operated by opening the constraints folder in the design sources box in Vivado.
10. You can see the layout using the Open Synthesized Design under the implementation window. Be sure to add the constraints again by removing previously unreachable constraints2.xdc file with the constraints2.xdc file present inside the code folder. From this you can observe the placement of the cells on the FPGA.
11. In case you want to setup the bitstream again you will need to reset the entire project as the references are incorrectly referenced.
12. For that you will need to add the IP based in PUF_interface_2/PUF_Interface_2/PUF_Interface_2/solution1/impl/ip to get the ap2axi data value convertor so as to communicate with the verilog block.
13. Add this and the ZYNQ PS to the block design and run block automation and connection automation. After that add the PUF.v IP block generated in the puf_final project and connect to the concerned cells.
14. The addresses that need to be read are provided in the interface's lowest HLS generated verilog file where each pin has the address on which data can be sent and read. Further info can be checked on the ipynb notebook.

Questions?
Raise issues if need be! 
