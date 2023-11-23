import os
import subprocess
import tkinter as tk
from tkinter import filedialog, ttk
from ttkthemes import ThemedTk
import urllib.request

def select_file(entry):
    filename = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def download_protein(entry):
    pdb_id = entry.get()
    url = f"https://files.rcsb.org/download/{pdb_id}.pdb"
    filename = f"{pdb_id}.pdb"
    urllib.request.urlretrieve(url, filename)
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def download_ligand(entry):
    cid = entry.get()
    url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/cid/{cid}/record/SDF/?record_type=3d&response_type=save"
    filename = f"{cid}.sdf"
    urllib.request.urlretrieve(url, filename)
    entry.delete(0, tk.END)
    entry.insert(0, filename)

def run_vina():
    receptor = receptor_entry.get()
    ligand = ligand_entry.get()
    config = config_entry.get()
    output = output_entry.get()
    image_output = image_entry.get()

    vina_cmd = f"vina --receptor {receptor} --ligand {ligand} --config {config} --out {output}"
    process = subprocess.Popen(vina_cmd, shell=True)
    process.wait()

    pymol_cmd = f"pymol -c -d 'load {output}; png {image_output}'"
    process = subprocess.Popen(pymol_cmd, shell=True)
    process.wait()

    os.startfile(output)
    os.startfile(image_output)

root = ThemedTk(theme="arc")  # Use um tema moderno

receptor_label = ttk.Label(root, text="Receptor:")
receptor_label.pack()
receptor_entry = ttk.Entry(root)
receptor_entry.pack()
receptor_button = ttk.Button(root, text="Select Receptor", command=lambda: select_file(receptor_entry))
receptor_button.pack()
receptor_download_button = ttk.Button(root, text="Download Protein", command=lambda: download_protein(receptor_entry))
receptor_download_button.pack()
receptor_download_button.bind("<Enter>", lambda e: receptor_download_button.config(text="Insira o ID PDB da proteína que deseja baixar e clique neste botão."))
receptor_download_button.bind("<Leave>", lambda e: receptor_download_button.config(text="Download Protein"))

ligand_label = ttk.Label(root, text="Ligand:")
ligand_label.pack()
ligand_entry = ttk.Entry(root)
ligand_entry.pack()
ligand_button = ttk.Button(root, text="Select Ligand", command=lambda: select_file(ligand_entry))
ligand_button.pack()
ligand_download_button = ttk.Button(root, text="Download Ligand", command=lambda: download_ligand(ligand_entry))
ligand_download_button.pack()
ligand_download_button.bind("<Enter>", lambda e: ligand_download_button.config(text="Insira o CID do ligante que deseja baixar e clique neste botão."))
ligand_download_button.bind("<Leave>", lambda e: ligand_download_button.config(text="Download Ligand"))

config_label = ttk.Label(root, text="Config:")
config_label.pack()
config_entry = ttk.Entry(root)
config_entry.pack()
config_button = ttk.Button(root, text="Select Config", command=lambda: select_file(config_entry))
config_button.pack()

output_label = ttk.Label(root, text="Output:")
output_label.pack()
output_entry = ttk.Entry(root)
output_entry.pack()

image_label = ttk.Label(root, text="Image Output:")
image_label.pack()
image_entry = ttk.Entry(root)
image_entry.pack()

run_button = ttk.Button(root, text="Run Vina", command=run_vina)
run_button.pack()

root.mainloop()