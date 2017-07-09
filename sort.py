import os

workdir = os.getcwd()
expdir = workdir + "/res"
prefix_drawable = "drawable-"
prefix_mipmap = "mipmap-"
densities_by_res = {"@0,25x": "mdpi",
                    "@0,38x": "hdpi",
                    "@0,5x": "xhdpi",
                    "@0,75x": "xxhdpi",
                    "@1x": "xxxhdpi",
                    "@NOx": "nodpi"}


def mkdir(prefix, dirname):
    currentpath = expdir + "/" + prefix
    if not os.path.exists(currentpath + dirname):
        os.makedirs(currentpath + dirname)


def set_prefix(filename):
    return prefix_mipmap if "ic_" in filename[0:3] else prefix_drawable


def get_dir_by_res(filename):
    res = "@1x"
    if "@" in filename:
        res = filename[filename.find("@"):filename.find(".")]
    print(filename)
    return set_prefix(filename)+densities_by_res[res]


def get_new_filename(filename):
    if '@' in filename:
        return filename[0:filename.find('@')] + filename[-4:]
    else:
        return filename


def replace_file(directory, filename):
    os.rename(workdir + '/' + filename,
              expdir + '/' + directory + '/' + get_new_filename(filename))


if __name__ == "__main__":
    for dir in densities_by_res:
        mkdir(prefix_mipmap, densities_by_res[dir])
        mkdir(prefix_drawable, densities_by_res[dir])

    for filename in os.listdir(workdir):
        if not filename[0] in ['.'] and not os.path.isdir(filename):
            get_dir_by_res(filename)
            replace_file(get_dir_by_res(filename), filename)
