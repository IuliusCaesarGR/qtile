from dbus import Interface
from libqtile import widget
from more_itertools import padded
from .theme import colors

# Get the icons at https://www.nerdfonts.com/cheat-sheet (you need a Nerd Font)

def base(fg='text', bg='dark'):
    return {
        'foreground': colors[fg],
        'background': colors[bg]
    }


def separator():
    return widget.Sep(**base(), linewidth=0, padding=5)


def icon(fg='text', bg='dark', fontsize=16, text="?"):
    return widget.TextBox(
        **base(fg, bg),
        fontsize=fontsize,
        text=text,
        padding=3
    )


def powerline(fg="light", bg="dark"):
    return widget.TextBox(
        **base(fg, bg),
        text="", # Icon: nf-oct-triangle_left
        fontsize=37,
        padding=-3
    )


def workspaces(): 
    return [
        separator(),
        widget.GroupBox(
            **base(fg='light'),
            font='UbuntuMono Nerd Font',
            fontsize=24,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=colors['active'],
            inactive=colors['inactive'],
            rounded=False,
            highlight_method='block',
            urgent_alert_method='block',
            urgent_border=colors['urgent'],
            this_current_screen_border=colors['focus'],
            this_screen_border=colors['grey'],
            other_current_screen_border=colors['dark'],
            other_screen_border=colors['dark'],
            disable_drag=True
        ),
        separator(),
        widget.WindowName(**base(fg='focus'), fontsize=14, padding=5),
        separator(),
    ]


primary_widgets = [
    *workspaces(),
    
    separator(),

    powerline('color5', 'dark'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    widget.CPU(**base(bg='color5'), padding=6, format='CPU {load_percent}%', update_interval=.5),
    widget.ThermalSensor(padding=5, **base(bg='color5'), threshold= 85),
    powerline('color4', 'color5'),
    widget.Memory( **base(bg='color4'), format= 'RAM {MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} | {MemPercent}%', padding=7, 	measure_mem='M', update_interval=.5),
    powerline('color3', 'color4'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color3'), padding=8, update_interval=.5, use_bits=False, format='{interface}: {down} ↓↑ {up}', prefix='k'),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    icon(bg="color1", fontsize=17, text=' '), # Icon: nf-mdi-calendar_clock

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),
    widget.Systray(background=colors['color1'], padding=5),

]

secondary_widgets = [
    *workspaces(),

    powerline('color5', 'dark'),

    icon(bg="color5", text=' '), # Icon: nf-fa-download
    widget.CPU(**base(bg='color5'), padding=6, format='CPU {load_percent}%', update_interval=.5),
    widget.ThermalSensor(padding=5, **base(bg='color5'), threshold= 85),
    powerline('color4', 'color5'),
    widget.Memory( **base(bg='color4'), format= 'RAM {MemUsed: .0f}{mm} /{MemTotal: .0f}{mm} | {MemPercent}%', padding=7, 	measure_mem='M', update_interval=.5),
    powerline('color3', 'color4'),

    icon(bg="color3", text=' '),  # Icon: nf-fa-feed

    widget.Net(**base(bg='color3'), padding=8, update_interval=.5, use_bits=False, format='{interface}: {down} ↓↑ {up}', prefix='k'),

    powerline('color2', 'color3'),

    widget.CurrentLayoutIcon(**base(bg='color2'), scale=0.65),

    widget.CurrentLayout(**base(bg='color2'), padding=5),

    powerline('color1', 'color2'),

    widget.Clock(**base(bg='color1'), format='%d/%m/%Y - %H:%M '),

    powerline('dark', 'dark'),
]

widget_defaults = {
    'font': 'UbuntuMono Nerd Font Bold',
    'fontsize': 16,
    'padding': 1,
}
extension_defaults = widget_defaults.copy()
