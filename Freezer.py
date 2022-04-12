# Copyright 2022 Cadwork Informatique Inc.
# All rights reserved.
# This file is part of Freezer,
# and is released under the "MIT License Agreement". Please see the LICENSE
# file that should have been included as part of this package.

import element_controller as ec
import menu_controller as mc
import visualization_controller as vc

# Localization: Edit this section
freeze_active_elements_menu_item = 'Freeze Active'
thaw_active_elements_menu_item = 'Thaw Active'
activate_frozen_elements_menu_item = 'Activate Frozen'
return_menu_item = 'Return'


def freeze_active_elements():
    active_elements = ec.get_active_identifiable_element_ids()
    vc.set_immutable(active_elements)


def thaw_active_elements():
    active_elements = ec.get_active_identifiable_element_ids()
    vc.set_mutable(active_elements)


def activate_frozen_elements():
    visible_elements = ec.get_visible_identifiable_element_ids()
    frozen_elements = []
    for element in visible_elements:
        if vc.is_immutable(element):
            frozen_elements.append(element)
    vc.set_inactive(visible_elements)
    vc.set_active(frozen_elements)


menu_items = [
    freeze_active_elements_menu_item,
    thaw_active_elements_menu_item,
    '',
    activate_frozen_elements_menu_item,
    '',
    return_menu_item
]

selected_menu_item = mc.display_simple_menu(menu_items)

if selected_menu_item == freeze_active_elements_menu_item:
    freeze_active_elements()
elif selected_menu_item == thaw_active_elements_menu_item:
    thaw_active_elements()
elif selected_menu_item == activate_frozen_elements_menu_item:
    activate_frozen_elements()
