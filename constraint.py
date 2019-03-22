
# generate .xdc file

x = open("constraints2.xdc", "w+")
l=['A','B','C','D']
number=35
for i in range(8):
    for j in range(16):
        if j%4==0:
            number=number+1
        path = "PUF_final_i/PUF_0/inst/PUF_id"+"["+str(i)+"].top/Tune/Coarse"+"["+str(j)+"].PC/Coarse"
        x.write("set_property BEL "+ l[j%4]+"LUT6 [get_cells \"" + path +"\"]")
        x.write('\n')
        x.write("set_property LOC SLICE_X"+str(number)+"Y90 "+ "[get_cells \""+ path + "\"]")
        x.write('\n')
        x.write('\n')


number=35
for i in range(0,8):
    for j in range(16):
        if j%4==0:
            number=number+1
        path = "PUF_final_i/PUF_0/inst/PUF_id"+"["+str(i)+"].bottom/Tune/Coarse"+"["+str(j)+"].PC/Coarse"
        x.write("set_property BEL "+ l[j%4]+"LUT6 [get_cells \"" + path +"\"]")
        x.write('\n')
        x.write("set_property LOC SLICE_X"+str(number)+"Y92 "+ "[get_cells \""+ path + "\"]")
        x.write('\n')
        x.write('\n')



number=36
for i in range(8):
    path = "PUF_final_i/PUF_0/inst/PUF_id"+"["+str(i)+"].arbiter"
    #x.write("set_property BEL "+ l[j%4]+"LUT6 [get_cells \"" + path +"\"]")
    #x.write('\n')
    x.write("set_property LOC SLICE_X"+ str(number)+"Y1 "+ "[get_cells \""+ path + "\"]")
    x.write('\n')
    x.write('\n')
    number=number+1

x.close()
