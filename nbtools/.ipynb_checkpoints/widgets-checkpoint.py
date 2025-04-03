
import mrich
import ipywidgets
from .requests import STACKS, target_list

def download():
    _download_ui_1()
    
    
def _download_ui_1():
    """Create widgets to request target list"""
    
    mrich.h1("download target")
    
    output = ipywidgets.Output()
    
    w_stack = ipywidgets.Dropdown(
        options=STACKS.keys(),
        value="production",
        description='Stack',
    )
    
    w_token = ipywidgets.Password(description="Token")
    
    b_get_targets = ipywidgets.Button(
        description='Get target list',
    )
    
    def button_func(button):
        with output:
            
    
    b_get_targets.on_click(button_func)
    
    display(w_stack, w_token, b_get_targets, output)


def button_func(button):
    with output:
        print("Button was clicked")


    
def _download_ui_2():
    """widgets to request target download"""
    raise NotImplementedError