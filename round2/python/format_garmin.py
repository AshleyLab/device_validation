import sys
import xml.etree.ElementTree as etree
import pdb
data=sys.argv[1]
outf=open(sys.argv[2],'w')
tree=etree.parse(data)
trackpoints=tree.findall('//'+'{http://www.garmin.com/xmlschemas/TrainingCenterDatabase/v2}Trackpoint')

for t in trackpoints:
    entry=[] 
    components=t.getchildren()
    for component in components:
        component_tag=component.tag
        if component_tag.__contains__('Time'):
            entry.append(component.text)
        elif component_tag.__contains__('HeartRateBpm'):
            hr=component.getchildren()[0].text
            entry.append(hr)
        if len(entry)==1:
            entry.append('')
    entry='\t'.join(entry)
    outf.write(entry+'\n')
    
            
            
