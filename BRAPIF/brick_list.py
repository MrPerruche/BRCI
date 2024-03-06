from dataclasses import dataclass
from BRAPIF import append_multiple

bd_materials = {
    'aluminium':        {'price': 2.00, 'density': 2.70, 'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'brushed aluminum': {'price': 2.00, 'density': 2.70, 'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'carbon':           {'price': 6.00, 'density': 1.55, 'strength': 10.0, 'friction': 0.70, 'restitution': 0.10},
    'traction plate':   {'price': 2.00, 'density': 2.70, 'strength': 7.50, 'friction': 0.57, 'restitution': 0.10},
    'chrome':           {'price': 2.00, 'density': 8.00, 'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'cloudy glass':     {'price': 1.50, 'density': 1.00, 'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'copper':           {'price': 3.00, 'density': 9.00, 'strength': 10.0, 'friction': 0.35, 'restitution': 0.10},
    'foam':             {'price': 0.50, 'density': 0.10, 'strength': 0.10, 'friction': 0.70, 'restitution': 0.10},
    'glass':            {'price': 1.50, 'density': 1.00, 'strength': 0.50, 'friction': 0.70, 'restitution': 0.10},
    'glow':             {'price': 1.50, 'density': 1.00, 'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'gold':             {'price': 11.0, 'density': 19.3, 'strength': 7.50, 'friction': 0.50, 'restitution': 0.10},
    'oak':              {'price': 1.00, 'density': 0.60, 'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'pine':             {'price': 1.00, 'density': 0.60, 'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'plastic':          {'price': 1.00, 'density': 1.00, 'strength': 3.00, 'friction': 0.60, 'restitution': 0.10},
    'old wood':         {'price': 0.75, 'density': 0.60, 'strength': 5.00, 'friction': 0.60, 'restitution': 0.10},
    'rubber':           {'price': 1.00, 'density': 1.00, 'strength': 3.00, 'friction': 2.00, 'restitution': 0.10},
    'rusted steel':     {'price': 3.00, 'density': 8.00, 'strength': 10.0, 'friction': 0.50, 'restitution': 0.10},
    'steel':            {'price': 4.00, 'density': 8.00, 'strength': 20.0, 'friction': 0.35, 'restitution': 0.10},
    'tungsten':         {'price': 8.50, 'density': 19.25, 'strength': 30.0, 'friction': 0.20, 'restitution': 0.10}
}


@dataclass
class BrickInput:

    brick_input_type: str
    brick_input: any

    def return_br(self):
        return b'01000700000006437573746F6D12496E7075744368616E6E656C2E56616C756501000400000000000040'  # TODO


# Bricks

br_brick_list = {
    '_default_brick' : {
        'BrickColor': [0, 0, 127, 255],
        'BrickPattern': 'Default',
        'BrickMaterial': 'Plastic',
        'Position': [0.0, 0.0, 0.0],
        'Rotation': [0.0, 0.0, 0.0]
    }
}

append_multiple(br_brick_list,['Switch_1sx1sx1s','Switch_1x1x1s'],
                br_brick_list['_default_brick'] | {
                    'OutputChannel.MinIn': -1,
                    'OutputChannel.MaxIn': 1,
                    'OutputChannel.MinOut': -1,
                    'OutputChannel.MaxOut': 1,
                    'InputChannel.InputAxis': BrickInput('None', None),
                    'bReturnToZero': True,
                    'SwitchName': ''}, True)

append_multiple(br_brick_list, ['DisplayBrick'],
                br_brick_list['_default_brick'] | {
                    'bGenerateLift': False,
                    'BrickSize': [6, 3, 1],
                    'ConnectorSpacing': [3, 3, 3, 3, 3, 3],
                    'InputChannel.InputAxis': BrickInput('Custom', None),
                    'NumFractionalDigits': 1,
                    'DisplayColor': [255, 255, 255, 255]
                }, True)