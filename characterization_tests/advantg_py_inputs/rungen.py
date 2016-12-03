'''
Created on Dec 2, 2016

@author: Mitch
'''
import utils
from copy import deepcopy

filepath = r'C:\\Users\\Mitch\\Documents\\Cal\\Slaybaugh_Group\\CaskModels\\char_tests\\'
geomname = 'maze1'

quads = ['qr','levelsym','glproduct']
triquadOs = [10,16,20]
prodquadOs = [2,4,10,16]
pnOs = [3]

def quaddepparam(quad,triquadOs,prodquadOs):
    # Set parameters dependent on quadrature type
    if quad == 'levelsym':
        filename = geomname + '_tri.py'     # specify triangular quad. type template
        optnames = ['denovo_quad_order']    # specify triangular quad. type labels
        quadOs = triquadOs                  # specify quadrature orders
    else:
        filename = geomname + '_prod.py'    # specify product quad. type template
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
        
                outputfile = open(filepath+filename[:-3]+'_%s%s-%s' %(quad,str(quadO),str(pnO))+'.py','w')           
                outputfile.write(output)
                outputfile.close()
                