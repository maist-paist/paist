from tkinter import filedialog


class Api:
    def get_file_to_read(self, default_dir):
        filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("VTK files", "*.vtk")))

        return {
            "file": filename
        }