#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# --------------------------------------------------------
# Faster R-CNN
# Copyright (c) 2015 Microsoft
# Licensed under The MIT License [see LICENSE for details]
# Written by Ross Girshick
# --------------------------------------------------------

"""
Demo script showing detections in sample images.

See README.md for installation instructions before running.
"""

import sys
import os
import shutil
import zipfile

def zip_dir(dirname,zipfilename):
    """
    | ##@函数目的: 压缩指定目录为zip文件
    | ##@参数说明：dirname为指定的目录，zipfilename为压缩后的zip文件路径
    | ##@返回值：无
    | ##@函数逻辑：
    """
    filelist = []

    zipf = zipfile.ZipFile(zipfilename, 'w', zipfile.ZIP_DEFLATED)
    # ziph is zipfile handle
    for root, dirs, files in os.walk(dirname):
        for file in files:
            ziph.write(os.path.join(root, file))
    zipf.close()
    # if os.path.isfile(dirname):
    #     filelist.append(dirname)
    # else :
    #     for root, dirs, files in os.walk(dirname):
    #         for name in files:
    #             filelist.append(os.path.join(root, name))


    # filelist = os.listdir(dirname)
 
    # zf = zipfile.ZipFile(zipfilename, "w", zipfile.zlib.DEFLATED)
    # for tar in filelist:
    #     arcname = tar[len(dirname):]
    #     #print arcname
    #     zf.write(tar,arcname)
    # zf.close()

def unzip_file(zipfilename, unziptodir):
    """
    | ##@函数目的: 解压zip文件到指定目录
    | ##@参数说明：zipfilename为zip文件路径，unziptodir为解压文件后的文件目录
    | ##@返回值：无
    | ##@函数逻辑：
    """
    if not os.path.exists(unziptodir):
        os.mkdir(unziptodir, 0777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\','/')
 
        if name.endswith('/'):
            p = os.path.join(unziptodir, name[:-1])
            if os.path.exists(p):
                # 如果文件夹存在，就删除之：避免有新更新无法复制
                shutil.rmtree(p)
            os.mkdir(p)
        else:
            ext_filename = os.path.join(unziptodir, name)
            ext_dir= os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir):
                os.mkdir(ext_dir,0777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def divide_img():
	FindPath = 'F:/Lab/Aesthetic_Quality/AVA_dataset/ImageSet/trainSet'
	fileNames = os.listdir(FindPath)
	print fileNames[:10]

	newPath = 'F:/Lab/Aesthetic_Quality/AVA_dataset/Divided_Set/trainSet'
	newPathList = [newPath+str(i+1) for i in range(10)]
	for item in newPathList:
		if not os.path.exists(item):
			os.mkdir(item)

	numPerPatch = 10 
	for i, fileName in enumerate(fileNames):
		index = i / numPerPatch
		if index >= len(newPathList):
			break
		shutil.copyfile(FindPath+'/'+fileName, newPathList[index]+'/'+fileName)

	zip_path = 'F:/Lab/Aesthetic_Quality/AVA_dataset/Divided_Set'
	shutil.make_archive(zip_path+'/trainSet'+str(0+1)+'.zip', 'zip', newPathList[0])
	# zip_dir(newPathList[0], zip_path+'/trainSet'+str(0+1)+'.zip')
	# for i, item in newPathList: 
	# 	zip_dir(item, zip_path+'/trainSet'+str(i+1)+'.zip')

if __name__ == '__main__':
	divide_img()
	# all_file = sys.argv[1]
	# curr_file = sys.argv[2]
	# save_file = sys.argv[3]

	# filter_valid(all_file, curr_file, save_file)

	#valid_count(f)