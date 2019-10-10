def replace_file_str(file_name, replace_str, new_str):
    data = ""
    with open(file_name, "r") as old_file:
        for line in old_file.readlines():
            if replace_str in line:
                line = line.replace(replace_str, new_str)
            data += line
    with open(file_name, "w") as new_file:
        new_file.write(data)


if __name__ == '__main__':
    # replace_file_str("./test.txt", "i915.avail_planes_per_pipe=0x070F00", "i915.avail_planes_per_pipe=0x000303")
    # replace_file_str("./test.txt", "i915.avail_planes_per_pipe=0x000303", "i915.avail_planes_per_pipe=0x070F00")

    ss = "m;5;208;1m/mnt/loader/entries/Clear-linux-kvm-5.2.13-385.confm"
    print(ss[ss.index("/mnt"): ss.index(".conf")+5])
