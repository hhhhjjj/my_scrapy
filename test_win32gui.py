import win32con
import win32gui
window_handle = win32gui.FindWindow(None, "打开")
ComboBoxEx32 = win32gui.FindWindowEx(window_handle, 0, 'ComboBoxEx32', None)
combobox_handle = win32gui.FindWindowEx(ComboBoxEx32, 0, "ComboBox", "")
edit_handle = win32gui.FindWindowEx(combobox_handle, 0, "Edit", None)
print(ComboBoxEx32)
print(combobox_handle)
print(edit_handle)
