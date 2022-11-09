import dearpygui.dearpygui as dpg
import model



dpg.create_context()

dpg.create_viewport(title='Star Travel',width=900,height=450)


with dpg.window(label='Probando...',width=900,height=450):
    
    dpg.add_text("Este es el programa para evaluar distacias",color=[255,0,0])
    dpg.add_combo(model.locations,default_value='Bucharest',label='Punto de partida',width=250,tag='locations')
    dpg.add_button(label='Obtener ruta óptima',tag='btnSearch')
    dpg.add_text('The best path is:',color=[223,0,0])
    initLocation = dpg.get_value('locations')
    dpg.set_item_callback('btnSearch',)

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()