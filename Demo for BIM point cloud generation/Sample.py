import pymeshlab as ml
import os

mesh_Rootpath = r'E:\实验数据\施工进度监测\model sample\data'                              # obj目录
mlx_path = r"E:\实验数据\施工进度监测\model sample\sample60000.mlx"             # mlx文件路径
tar_Rootpath = r"E:\output"                         # 点云文件目录

mesh_list = os.listdir(mesh_Rootpath)
for m in mesh_list:                                             # m是每个obj文件的名字，e.g.1.obj
    if m[-3:] == "ply":                                         # mesh的路径下既有obj文件也有mtl材质文件，只读取obj文件
        m_name = m[:-4]                                         # m_name是没有后缀的文件名
        mesh_path = os.path.join(mesh_Rootpath, m)              # mesh的路径
        tar_path = os.path.join(tar_Rootpath, m_name+".xyz")    # mesh对应点云的路径
        ms = ml.MeshSet()
        ms.load_new_mesh(mesh_path)
        ms.load_filter_script(mlx_path)
        ms.apply_filter_script()
        ms.save_current_mesh(tar_path)
        print("Finished %s, get %s" % (m, m_name+".xyz"))

