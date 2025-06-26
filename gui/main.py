import forget_me_not as fmn
import slot
import dearpygui.dearpygui as dpg

def main():
    # Serial Modifier
    def serial_right():
        serial = dpg.get_value("Serial")
        global right_serial
        serial_list = list(serial)
        if len(serial_list) == 6:
            return int(serial_list[5])
        else:
            ValueError("Serial number must be 6 digits long.")

    def serial_largest_num():
        serial = dpg.get_value("Serial")
        serial_num_list = []
        for i in serial:
            if i.isdigit():
                serial_num_list.append(int(i))
        serial_num_largest = serial_num_list[0]
        for i in serial_num_list:
            if i > serial_num_largest:
                serial_num_largest = i
        return int(serial_num_largest)
    
    # Functions that call the modules
    def forget_me_not_call():
        serial = dpg.get_value("Serial")
        number = dpg.get_value("Numbers")
        unlit_car = dpg.get_value("Unlit Car")
        unlit = int(dpg.get_value("Unlit Total"))
        lit = int(dpg.get_value("Lit Total"))
        serial_port = dpg.get_value("Serial Port")

        final_list = fmn.forget_me_not(serial, number, unlit_car, unlit, lit, serial_port)
        dpg.set_value("Final List", str(final_list))

    def slots_call():
        lit = int(dpg.get_value("Lit Total"))
        unlit = int(dpg.get_value("Unlit Total"))
        rca_ps2 = dpg.get_value("RCA/PS2")
        parallel = dpg.get_value("Parallel")
        full_list = dpg.get_value("Full List")
        unlit_bob = dpg.get_value("Unlit BOB")
        battery = int(dpg.get_value("Batteries"))
        serial_port = dpg.get_value("Serial Port")

        final_slots = slot.slot(lit, unlit, rca_ps2, full_list, battery, parallel, serial_right(), unlit_bob, serial_port, serial_largest_num())
        dpg.set_value("Final Slots", str(final_slots))

    # Gui Section

    dpg.create_context()
    dpg.create_viewport(title='KTANE Tools', width=455, height=455, min_width=455, min_height=455, max_width=455, max_height=455)

    with dpg.window(label="Combined Info", height=220, width=240, pos=(0, 0), no_resize=True, no_move=True, no_collapse=True):
        dpg.add_text("Enter Serial Number:")
        dpg.add_input_text(tag="Serial", default_value="")

        dpg.add_text("Serial Port Present:")
        dpg.add_checkbox(tag="Serial Port", default_value=False)

        dpg.add_text("Enter Amount of Unlit Indicators:")
        dpg.add_input_int(tag="Unlit Total", default_value=0)

        dpg.add_text("Enter Amount of Lit Indicators:")
        dpg.add_input_int(tag="Lit Total", default_value=0)

    with dpg.window(label="Forget Me Not", height=200, width=240, pos=(0, 220), no_resize=True, no_move=True, no_collapse=True):

        dpg.add_text("Enter Numbers:")
        dpg.add_input_text(tag="Numbers", default_value="")


        dpg.add_text("Unlit Indicators (Car):")
        dpg.add_checkbox(tag="Unlit Car", default_value=False)

        
        dpg.add_button(label="Calculate", callback=forget_me_not_call)

        dpg.add_text("Final List:")
        dpg.add_text("", tag="Final List")

    with dpg.window(label="Slots", height=420, width=200,pos=(240, 0), no_resize=True, no_move=True, no_collapse=True):

        dpg.add_text("RCA/PS2 Present:")
        dpg.add_checkbox(tag="RCA/PS2", default_value=False)

        dpg.add_text("Enter Full List of Slots:")
        dpg.add_input_text(tag="Full List", default_value="")

        dpg.add_text("Parallel Present:")
        dpg.add_checkbox(tag="Parallel", default_value=False)

        dpg.add_text("Enter Amount of Batteries:")
        dpg.add_input_int(tag="Batteries", default_value=0)

        dpg.add_text("Unlit BOB Present:")
        dpg.add_checkbox(tag="Unlit BOB", default_value=False)


        dpg.add_button(label="Calculate Slots", callback=slots_call)

        dpg.add_text("Final Slot Numbers:")
        dpg.add_text("", tag="Final Slots")
    # Setup and start Dear PyGui
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()

