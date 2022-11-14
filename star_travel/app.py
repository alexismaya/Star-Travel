import dearpygui.dearpygui as dpg
import model



def searchCall():
    initLocation = dpg.get_value('locations')
    bestPath = model.aStarSearch(initLocation)
    dpg.set_value('txtPath', bestPath)

dpg.create_context()

dpg.create_viewport(title='Star Travel',width=900,height=450)


with dpg.window(label='Probando...',width=900,height=450):
    
    dpg.add_text("Este es el programa para evaluar distacias",color=[255,0,0])
    dpg.add_combo(model.locations,default_value='Bucharest',label='Punto de partida',width=250,tag='locations')
    dpg.add_text('The best path is:',color=[223,0,0],tag='txtPath')
    dpg.add_button(label='Obtener ruta óptima',tag='btnSearch',callback=searchCall)
    
with dpg.theme() as global_theme:

    with dpg.theme_component(dpg.mvAll):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (30, 30, 46), category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)
        
    with dpg.theme_component(dpg.mvButton):
        dpg.add_theme_color(dpg.mvThemeCol_Button,(18, 153, 82),category=dpg.mvThemeCat_Core)
        
    with dpg.theme_component(dpg.mvInputInt):
        dpg.add_theme_color(dpg.mvThemeCol_FrameBg, (30, 30, 46), category=dpg.mvThemeCat_Core)
        dpg.add_theme_color(dpg.mvThemeCol_Button,(18, 153, 82),category=dpg.mvThemeCat_Core)
        dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 5, category=dpg.mvThemeCat_Core)

dpg.bind_theme(global_theme)

dpg.show_style_editor()


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()