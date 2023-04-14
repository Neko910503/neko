
from qiskit_metal.qlibrary.tlines.meandered import RouteMeander

from qiskit_metal.qlibrary.qubits.transmon_pocket_6 import TransmonPocket6

from qiskit_metal.qlibrary.terminations.launchpad_wb_coupled import LaunchpadWirebondCoupled

from qiskit_metal import designs, MetalGUI

design = designs.DesignPlanar()

gui = MetalGUI(design)



            # WARNING
#options_connection_pads failed to have a value
Q_Main = TransmonPocket6(
design,
name='Q_Main',
options={'connection_pads': {'bus_00': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '30um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '10um',
                                'pad_height': '30um',
                                'pad_width': '60um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '10um',
                                'pad_height': '30um',
                                'pad_width': '60um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_03': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '30um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_04': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '10um',
                                'pad_height': '30um',
                                'pad_width': '60um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_05': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '10um',
                                'pad_height': '30um',
                                'pad_width': '60um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pad_width': '425 um',
 'pos_x': '0mm',
 'pos_y': '-1mm'}
)





            # WARNING
#options_connection_pads failed to have a value
Q1 = TransmonPocket6(
design,
name='Q1',
options={'connection_pads': {'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'readout': {'cpw_extend': '100um',
                                 'cpw_gap': '6um',
                                 'cpw_width': '10um',
                                 'loc_H': 1,
                                 'loc_W': 0,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '0um',
                                 'pad_gap': '50um',
                                 'pad_height': '30um',
                                 'pad_width': '80um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pos_x': '-3mm',
 'pos_y': '0.5mm'}
)





            # WARNING
#options_connection_pads failed to have a value
Q2 = TransmonPocket6(
design,
name='Q2',
options={'connection_pads': {'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_03': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'readout': {'cpw_extend': '100um',
                                 'cpw_gap': '6um',
                                 'cpw_width': '10um',
                                 'loc_H': 1,
                                 'loc_W': 0,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '0um',
                                 'pad_gap': '50um',
                                 'pad_height': '30um',
                                 'pad_width': '80um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pos_x': '0mm',
 'pos_y': '1mm'}
)





            # WARNING
#options_connection_pads failed to have a value
Q3 = TransmonPocket6(
design,
name='Q3',
options={'connection_pads': {'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': -1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'readout': {'cpw_extend': '100um',
                                 'cpw_gap': '6um',
                                 'cpw_width': '10um',
                                 'loc_H': 1,
                                 'loc_W': 0,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '0um',
                                 'pad_gap': '50um',
                                 'pad_height': '30um',
                                 'pad_width': '80um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pos_x': '3mm',
 'pos_y': '0.5mm'}
)





            # WARNING
#options_connection_pads failed to have a value
Q4 = TransmonPocket6(
design,
name='Q4',
options={'connection_pads': {'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'readout': {'cpw_extend': '100um',
                                 'cpw_gap': '6um',
                                 'cpw_width': '10um',
                                 'loc_H': -1,
                                 'loc_W': 0,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '0um',
                                 'pad_gap': '50um',
                                 'pad_height': '30um',
                                 'pad_width': '80um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pos_x': '-3mm',
 'pos_y': '-2.5mm'}
)





            # WARNING
#options_connection_pads failed to have a value
Q5 = TransmonPocket6(
design,
name='Q5',
options={'connection_pads': {'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_03': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'readout': {'cpw_extend': '100um',
                                 'cpw_gap': '6um',
                                 'cpw_width': '10um',
                                 'loc_H': -1,
                                 'loc_W': 0,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '0um',
                                 'pad_gap': '50um',
                                 'pad_height': '30um',
                                 'pad_width': '80um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pos_x': '0mm',
 'pos_y': '-3mm'}
)





            # WARNING
#options_connection_pads failed to have a value
Q6 = TransmonPocket6(
design,
name='Q6',
options={'connection_pads': {'bus_01': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': 0,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'bus_02': {'cpw_extend': '100um',
                                'cpw_gap': '6um',
                                'cpw_width': '10um',
                                'loc_H': 1,
                                'loc_W': -1,
                                'pad_cpw_extent': '25um',
                                'pad_cpw_shift': '0um',
                                'pad_gap': '15um',
                                'pad_height': '30um',
                                'pad_width': '80um',
                                'pocket_extent': '5um',
                                'pocket_rise': '0um'},
                     'readout': {'cpw_extend': '100um',
                                 'cpw_gap': '6um',
                                 'cpw_width': '10um',
                                 'loc_H': -1,
                                 'loc_W': 0,
                                 'pad_cpw_extent': '25um',
                                 'pad_cpw_shift': '0um',
                                 'pad_gap': '50um',
                                 'pad_height': '30um',
                                 'pad_width': '80um',
                                 'pocket_extent': '5um',
                                 'pocket_rise': '0um'}},
 'gds_cell_name': 'FakeJunction_01',
 'hfss_inductance': '14nH',
 'pos_x': '3mm',
 'pos_y': '-2.5mm'}
)




Bus_01 = RouteMeander(
design,
name='Bus_01',
options={'_actual_length': '11.713695323611194 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '50um',
          'start_jogged_extension': '',
          'start_straight': '946um'},
 'meander': {'asymmetry': '450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q_Main',
                            'pin': 'bus_02'},
                'start_pin': {'component': 'Q1',
                              'pin': 'bus_01'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_02 = RouteMeander(
design,
name='Bus_02',
options={'_actual_length': '11.783791666666662 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '50um',
          'start_jogged_extension': '',
          'start_straight': '43.5um'},
 'meander': {'asymmetry': '450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q_Main',
                            'pin': 'bus_01'},
                'start_pin': {'component': 'Q4',
                              'pin': 'bus_01'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_03 = RouteMeander(
design,
name='Bus_03',
options={'_actual_length': '11.783791666666668 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '50um',
          'start_jogged_extension': '',
          'start_straight': '43.5um'},
 'meander': {'asymmetry': '450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q_Main',
                            'pin': 'bus_04'},
                'start_pin': {'component': 'Q3',
                              'pin': 'bus_01'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_04 = RouteMeander(
design,
name='Bus_04',
options={'_actual_length': '11.713695323611194 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '50um',
          'start_jogged_extension': '',
          'start_straight': '946um'},
 'meander': {'asymmetry': '450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q_Main',
                            'pin': 'bus_05'},
                'start_pin': {'component': 'Q6',
                              'pin': 'bus_01'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_05 = RouteMeander(
design,
name='Bus_05',
options={'_actual_length': '6.000000000000002 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '0um'},
 'pin_inputs': {'end_pin': {'component': 'Q_Main',
                            'pin': 'bus_03'},
                'start_pin': {'component': 'Q2',
                              'pin': 'bus_01'}},
 'total_length': '6mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_06 = RouteMeander(
design,
name='Bus_06',
options={'_actual_length': '5.999999999999999 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '0um',
          'start_jogged_extension': '',
          'start_straight': '0um'},
 'pin_inputs': {'end_pin': {'component': 'Q_Main',
                            'pin': 'bus_00'},
                'start_pin': {'component': 'Q5',
                              'pin': 'bus_01'}},
 'total_length': '6mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_07 = RouteMeander(
design,
name='Bus_07',
options={'_actual_length': '12.0 mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '50um',
          'start_jogged_extension': '',
          'start_straight': '43.5um'},
 'meander': {'asymmetry': '450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q2',
                            'pin': 'bus_02'},
                'start_pin': {'component': 'Q1',
                              'pin': 'bus_02'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_08 = RouteMeander(
design,
name='Bus_08',
options={'_actual_length': '12.0 mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '120um',
          'start_jogged_extension': '',
          'start_straight': '0um'},
 'meander': {'asymmetry': '-450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q2',
                            'pin': 'bus_03'},
                'start_pin': {'component': 'Q3',
                              'pin': 'bus_02'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_09 = RouteMeander(
design,
name='Bus_09',
options={'_actual_length': '11.999999999999995 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '120um',
          'start_jogged_extension': '',
          'start_straight': '0um'},
 'meander': {'asymmetry': '-450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q5',
                            'pin': 'bus_03'},
                'start_pin': {'component': 'Q4',
                              'pin': 'bus_02'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Bus_10 = RouteMeander(
design,
name='Bus_10',
options={'_actual_length': '11.999999999999998 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '43.5um',
          'start_jogged_extension': '',
          'start_straight': '50um'},
 'meander': {'asymmetry': '450um',
             'spacing': '200um'},
 'pin_inputs': {'end_pin': {'component': 'Q5',
                            'pin': 'bus_02'},
                'start_pin': {'component': 'Q6',
                              'pin': 'bus_02'}},
 'total_length': '12mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Launch_Q1_Read = LaunchpadWirebondCoupled(
design,
name='Launch_Q1_Read',
options={'orientation': '270',
 'pos_x': '-3mm',
 'pos_y': '2.5mm'},

component_template=None,
)




Launch_Q2_Read = LaunchpadWirebondCoupled(
design,
name='Launch_Q2_Read',
options={'orientation': '270',
 'pos_x': '0mm',
 'pos_y': '2.5mm'},

component_template=None,
)




Launch_Q3_Read = LaunchpadWirebondCoupled(
design,
name='Launch_Q3_Read',
options={'orientation': '270',
 'pos_x': '3mm',
 'pos_y': '2.5mm'},

component_template=None,
)




Launch_Q4_Read = LaunchpadWirebondCoupled(
design,
name='Launch_Q4_Read',
options={'orientation': '90',
 'pos_x': '-3mm',
 'pos_y': '-4.5mm'},

component_template=None,
)




Launch_Q5_Read = LaunchpadWirebondCoupled(
design,
name='Launch_Q5_Read',
options={'orientation': '90',
 'pos_x': '0mm',
 'pos_y': '-4.5mm'},

component_template=None,
)




Launch_Q6_Read = LaunchpadWirebondCoupled(
design,
name='Launch_Q6_Read',
options={'orientation': '90',
 'pos_x': '3mm',
 'pos_y': '-4.5mm'},

component_template=None,
)




Read_Q1 = RouteMeander(
design,
name='Read_Q1',
options={'_actual_length': '5.0 mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '125um',
          'start_jogged_extension': '',
          'start_straight': '125um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_Q1_Read',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q1',
                              'pin': 'readout'}},
 'total_length': '5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Read_Q2 = RouteMeander(
design,
name='Read_Q2',
options={'_actual_length': '10.000000000000002 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '125um',
          'start_jogged_extension': '',
          'start_straight': '125um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_Q2_Read',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q2',
                              'pin': 'readout'}},
 'total_length': '10mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Read_Q3 = RouteMeander(
design,
name='Read_Q3',
options={'_actual_length': '5.0 mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '125um',
          'start_jogged_extension': '',
          'start_straight': '125um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_Q3_Read',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q3',
                              'pin': 'readout'}},
 'total_length': '5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Read_Q4 = RouteMeander(
design,
name='Read_Q4',
options={'_actual_length': '5.000000000000002 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '125um',
          'start_jogged_extension': '',
          'start_straight': '125um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_Q4_Read',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q4',
                              'pin': 'readout'}},
 'total_length': '5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Read_Q5 = RouteMeander(
design,
name='Read_Q5',
options={'_actual_length': '10.0 mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '125um',
          'start_jogged_extension': '',
          'start_straight': '125um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_Q5_Read',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q5',
                              'pin': 'readout'}},
 'total_length': '10mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)




Read_Q6 = RouteMeander(
design,
name='Read_Q6',
options={'_actual_length': '5.000000000000002 '
                   'mm',
 'fillet': '99um',
 'hfss_wire_bonds': True,
 'lead': {'end_jogged_extension': '',
          'end_straight': '125um',
          'start_jogged_extension': '',
          'start_straight': '125um'},
 'pin_inputs': {'end_pin': {'component': 'Launch_Q6_Read',
                            'pin': 'tie'},
                'start_pin': {'component': 'Q6',
                              'pin': 'readout'}},
 'total_length': '5mm',
 'trace_gap': 'cpw_gap'},

type='CPW',
)



gui.rebuild()
gui.autoscale()
        