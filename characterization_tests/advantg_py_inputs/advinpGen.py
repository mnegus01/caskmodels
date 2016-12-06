'''
Created on Dec 2, 2016
@author: Mitch

Python script to prepare ADVANTG simulations
    Before running:     -Provide path to input templates
                        -Provide name of geometry
                        -List quadrature types (Quadruple range, Level-Symmetric, or Gauss-Legendre)
                        -List quadrature orders (order # for tri-LS; quad angle # for prod-QR,GL)
                        -List P_N orders
                        -Choose whether to generate python ADVANTG inputs, BASH runscripts for an input, or both
'''
import utils
import runscriptGen as rsG
from copy import deepcopy


filepath = r'C:\\Users\\Mitch\\Documents\\Cal\\Slaybaugh_Group\\CaskModels\\char_tests\\'
geomname = 'maze1'

quads = ['qr','levelsym','glproduct']
triquadOs = [10,16,20]
prodquadOs = [2,4,10,16]
pnOs = [3]

ADVANTGrun = 1  # 1 to generate ADVANTG (python) inputs
SLURMrun = 1    # 1 to generate corresponding runscripts


def quaddepparam(quad,triquadOs,prodquadOs):
    # Set parameters dependent on quadrature type
    if quad == 'levelsym':
        filename = geomname + '_t.py'     # specify triangular quad. type template
        optnames = ['denovo_quad_order']    # specify triangular quad. type labels
        quadOs = triquadOs                  # specify quadrature orders
    else:
        filename = geomname + '_p.py'    # specify product quad. type template
        optnames = ['denovo_quad_num_azi','denovo_quad_num_polar']
        quadOs = prodquadOs                 # specify quadrature angle numbers
        
    return filename,optnames,quadOs


def changeoptions(template,option,newvalue):
    # Given a specific option, change the existing value to the new value 
    for line in changedlist:
        if line[0].strip(' \"\t') == option:
            if isinstance(newvalue,str):
                line[1] = '"' + newvalue + '",'
            else:
                line[1] = str(newvalue) + ','
            
    return changedlist


if __name__ == '__main__':
    
    for quad in quads:
        
        filename,optnames,quadOs = quaddepparam(quad,triquadOs,prodquadOs)
            
        templatefile = open(filepath+filename,'r')
        template = utils.splitfile(templatefile,':')
        templatefile.close()
        changedlist = deepcopy(template)
        
        # Update to reflect quadrature type
        changedlist = changeoptions(template,'denovo_quadrature',quad)

        for quadO in quadOs:
            # Update to reflect quarature order 
            for optname in optnames:
                changedlist = changeoptions(template,optname,quadO)

            for pnO in pnOs:
                changedlist = changeoptions(template,'denovo_pn_order',pnO)
                output = utils.joinfile(changedlist,':\t')
        
                runname = filename[:-5]+'_%s%s-%s' %(quad,str(quadO),str(pnO))
                
                if ADVANTGrun == 1:
                    outputfile = open(filepath+runname+'.py','w')
                    outputfile.write(output)
                    outputfile.close()
                if SLURMrun == 1:
                    runscriptfile = open(filepath+runname+'.sh','w')
                    runscriptfile.write(rsG.makerunscript(runname))
                    runscriptfile.close()
                    
                    
                