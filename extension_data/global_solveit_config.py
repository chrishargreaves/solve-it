

"""
This provides default code for determining what colour is used 
for presenting techniques in the main 
"""
def get_colour_for_technique(kb, t_id):
    t = kb.get_technique(t_id)
    
    # checks number of weaknesses and returns 
    # a different colour for those with zero
    # (as a proxy for how well developed the 
    # technique is)

    if len(t.get('weaknesses')) == 0:
        return "#F4CCCC" # consider this as placholder
    elif (t.get('description') is None or t.get('description') == "") or len(kb.get_mit_list_for_technique(t_id)) == 0:
        return "#FCE5CD" # consider this as partially populated
    else:
        return "#D9EAD3" # consider this as a release candidate
