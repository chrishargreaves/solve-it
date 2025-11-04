

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
        return "#F8F8F8"
    else:
        return "#E9E9E9"
