#!/usr/bin/python3

"""
Aaron's Personal Dashboard for Ampere³ System
"""

def create_subdialogwindow(parent):
    """Create Aaron's personal dashboard window"""
    try:
        import gi
        gi.require_version('Gtk', '3.0')
        from gi.repository import Gtk
        
        dialog = Gtk.Dialog("Aaron's Dashboard", parent, 0)
        dialog.set_decorated(False)
        dialog.maximize()
        dialog.set_name("backed_bg")
        
        content_area = dialog.get_content_area()
        
        # Main container
        main_box = Gtk.VBox(spacing=20)
        main_box.set_border_width(30)
        
        # Title
        title = Gtk.Label()
        title.set_markup("<span font='20' color='#FFD700' weight='bold'>👨‍💻 Aaron's Personal Dashboard</span>")
        title.set_justify(Gtk.Justification.CENTER)
        main_box.pack_start(title, False, False, 10)
        
        # Stats grid
        stats_grid = Gtk.Grid()
        stats_grid.set_column_spacing(40)
        stats_grid.set_row_spacing(20)
        stats_grid.set_halign(Gtk.Align.CENTER)
        
        # Stat boxes
        stats = [
            ("🎯", "Sessions Today", "3"),
            ("⏱️", "Total Time", "2.5 hrs"),
            ("🤖", "Gestures Learned", "12"),
            ("📊", "Accuracy Rate", "94%"),
            ("🔋", "Battery Level", "87%"),
            ("📡", "Signal Quality", "Excellent")
        ]
        
        row = 0
        col = 0
        for icon, label, value in stats:
            stat_box = Gtk.VBox(spacing=5)
            stat_box.set_size_request(150, 100)
            
            icon_label = Gtk.Label()
            icon_label.set_markup("<span font='24'>%s</span>" % icon)
            stat_box.pack_start(icon_label, False, False, 0)
            
            value_label = Gtk.Label()
            value_label.set_markup("<span font='18' color='#FFD700' weight='bold'>%s</span>" % value)
            stat_box.pack_start(value_label, False, False, 0)
            
            desc_label = Gtk.Label()
            desc_label.set_markup("<span font='12' color='#FFFFFF'>%s</span>" % label)
            stat_box.pack_start(desc_label, False, False, 0)
            
            stats_grid.attach(stat_box, col, row, 1, 1)
            
            col += 1
            if col >= 3:
                col = 0
                row += 1
        
        main_box.pack_start(stats_grid, True, True, 20)
        
        # Quick actions
        actions_label = Gtk.Label()
        actions_label.set_markup("<span font='16' color='#FFFFFF' weight='bold'>Quick Actions</span>")
        main_box.pack_start(actions_label, False, False, 10)
        
        actions_box = Gtk.HBox(spacing=20)
        actions_box.set_halign(Gtk.Align.CENTER)
        
        action_buttons = [
            "🎯 Start Training",
            "📊 View Reports", 
            "⚙️ Settings",
            "🔄 Sync Data"
        ]
        
        for button_text in action_buttons:
            btn = Gtk.Button(button_text)
            btn.set_size_request(120, 40)
            actions_box.pack_start(btn, False, False, 0)
        
        main_box.pack_start(actions_box, False, False, 20)
        
        content_area.add(main_box)
        
        # Connect close events
        dialog.connect("key-press-event", lambda w, e: dialog.destroy() if e.keyval == 65307 else None)  # ESC key
        dialog.connect("button-press-event", lambda w, e: dialog.destroy())
        
        dialog.show_all()
        dialog.run()
        dialog.destroy()
        
    except Exception as e:
        print(f"Aaron Dashboard Error: {e}")
        # Fallback message
        print("=== AARON'S DASHBOARD ===")
        print("👨‍💻 Personal Stats:")
        print("  🎯 Sessions Today: 3")
        print("  ⏱️ Total Time: 2.5 hrs") 
        print("  🤖 Gestures Learned: 12")
        print("  📊 Accuracy Rate: 94%")
        print("  🔋 Battery Level: 87%")
        print("  📡 Signal Quality: Excellent")
        print("========================")
