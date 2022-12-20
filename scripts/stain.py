import hou

from colorschemes import *
# from overwrite import *


#\/#------------------------------initialize--------------------------------#\/#
def createdestroy_func(kwargs):
    node = kwargs['node']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    ops = node.parm('vis').eval()
    for x in range(ops):
        if (x + 1) > len(vistup):        
            vis = hou.viewportVisualizers.createVisualizer(
                hou.viewportVisualizers.type('vis_color'),
                hou.viewportVisualizerCategory.Node,
                node
            )
            vis.setIsActive(True, None)
            vis.setParm('colortype', 1)
            vis.setParm('rangespec', 1)
            vis.setParm('clamptype', 1)
            vis.setParm('colorramp', 0)
            ramp = node.parm('ramp' + str(x))
            preset = node.parm('presets' + str(x)).evalAsString()
            ramp.set(globals()[preset], None, False)
        if ops < len(vistup) and (x + 2) == len(vistup):
            vis = vistup[x + 1]
            vis.destroy()
    if ops == 0:
        vis = vistup[0]
        vis.destroy()
#/\#------------------------------initialize--------------------------------#/\#


#\/#------------------------------global funcs------------------------------#\/#
def enable_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    enable = parm.eval()
    if enable == 1:
        vis.setIsActive(True, None)
    if enable == 0:
        vis.setIsActive(False, None)

def attr_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    attr = parm.eval()
    vis.setParm('attrib', attr)
    vis.setLabel(attr)

def datatype_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistypes = hou.viewportVisualizers.types()
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    type = parm.eval()
    if type == 0:
        vis.setType(vistypes[1])
    if type == 1:
        vis.setType(vistypes[0])
        vis.setParm('style', 4)
        coloring_func(kwargs)

def color_func(kwargs):
    node = kwargs['node']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    index = kwargs['script_multiparm_index']
    colorr = node.parm('color' + index + 'r').eval()
    colorg = node.parm('color' + index + 'g').eval()
    colorb = node.parm('color' + index + 'b').eval()
    vis = vistup[int(index)]
    vis.setParm('markercolorr', colorr)
    vis.setParm('markercolorg', colorg)
    vis.setParm('markercolorb', colorb)
#/\#------------------------------global funcs------------------------------#/\#


#\/#------------------------------ramp funcs--------------------------------#\/#
def presets_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    preset = node.parm('presets' + index).evalAsString()
    ramp = node.parm('ramp' + index)

    ramp.set(globals()[preset], None, False)
    ramp_func(kwargs)

def ramp_func(kwargs):
    node = kwargs['node']
    nesting = int(kwargs['script_multiparm_nesting'])
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    index = 'undefined'
    if nesting == 1:
        index = kwargs['script_multiparm_index']
    if nesting > 1:
        index = kwargs['script_multiparm_index2']
    indexint = int(index)
    vis = vistup[indexint]
    ramp = node.parm('ramp' + index).eval()
    vis.setParm('colorramp', ramp)

def overwrite_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']
    ramp = node.parm('ramp' + index).eval()
    preset = str(node.parm('presets' + index).evalAsString())
    scheme = 'candypeach = hou.Ramp(' + str(ramp.basis()) + ', ' + str(ramp.keys()) + ', ' + str(ramp.values()) + ') \n'
    # with open('C:/Users/lucas/OneDrive/Git/morphogen/scripts/overwrite.py', 'a') as append:
    #     append.write(scheme)
    test = hou.ui.readInput("Overwrite Preset?", ("Yes", "Cancel"), hou.severityType.Message, 0, -1, None, None, preset)

def rename_func(kwargs):

    node = kwargs['node']

    index = kwargs['script_multiparm_index']

    group = node.parmTemplateGroup()

    presets = node.parm('presets' + index)
    template = presets.parmTemplate()

    

    presetindex = presets.evalAsInt()

    menuitems = presets.menuItems()
    menuitems = list(menuitems)
    menuitems[int(presetindex)] = "farmer"
    menuitems = tuple(menuitems)

    
    entries = group.entries()
    folder = group.find('vis')
    templates = folder.parmTemplates()

    print(template)
    print()
    print(entries)
    # template = presets.menuItems()

#/\#------------------------------ramp funcs--------------------------------#/\#


#\/#------------------------------float funcs-------------------------------#\/#
def rampattr_func(kwargs):
    node = kwargs['node']
    parm = kwargs['node']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    rampattr = parm.eval()
    vis.setParm('attrib', rampattr)
#/\#------------------------------float funcs-------------------------------#/\#


#\/#------------------------------vec funcs---------------------------------#\/#
def coloring_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    coloring = node.parm('coloring' + index).eval()
    vis.setParm('vectorcoloring', coloring)
    if coloring == 0:
        color_func(kwargs)
    if coloring != 0:
        vis.setParm('ramptype', 6)
        vis.setParm('rangespec', 0 )
    if coloring == 3:
        colorattr_func(kwargs)

def lengthscale_func(kwargs):
    node = kwargs['node']
    parm = kwargs['parm']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    lengthscale = parm.eval()
    vis.setParm('lengthscale', lengthscale)

def colorattr_func(kwargs):
    node = kwargs['node']
    index = kwargs['script_multiparm_index']
    vistup = hou.viewportVisualizers.visualizers(
        hou.viewportVisualizerCategory.Node,
        node
    )
    vis = vistup[int(index)]
    colorattr = node.parm('colorattr' + index).eval()
    vis.setParm('colorattrib', colorattr)
#/\#------------------------------vec funcs---------------------------------#/\#

