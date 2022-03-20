import glob
import pprint
import csv


# get lines between <bmp_begin> and <bmp_end> delimiters
def get_bmp_lines(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
        bmp_lines = []
        bmp_begin = False
        bmp_end = False
        for line in lines:
            if line.startswith('<bmp_begin>'):
                bmp_begin = True
            if line.startswith('<bmp_end>'):
                bmp_end = True
            if bmp_begin and not bmp_end:
                bmp_lines.append(line)
        return bmp_lines


# walking_frame_rate 3
# walking_speed 5.000000
# walking_speedz 2.500000
# running_frame_rate 3
# running_speed 9.300000
# running_speedz 1.560000
# heavy_walking_speed 3.700000
# heavy_walking_speedz 1.850000
# heavy_running_speed 6.200000
# heavy_running_speedz 1.000000
# jump_height -16.299999
# jump_distance 10.000000
# jump_distancez 3.750000
# dash_height -10.000000
# dash_distance 18.000000
# dash_distancez 5.000000
# rowing_height -2.000000
# rowing_distance 5.000000
# Create a map of the values
def get_values(bmp_lines):
    values = {}
    for line in bmp_lines:
        line = line.strip()
        if line.startswith('<'):
            continue
        line = line.split(' ')
        key = line[0]

        # if key contains file, skip it
        if key.startswith('file'):
            continue

        value = line[1]
        values[key] = value
    return values


if __name__ == '__main__':
    # read all files at  ./data_files_decrypted
    files = glob.glob('./data_files_decrypted/*.txt')

    chars = {
        'template',
        'julian',
        'firzen',
        'louisEX',
        'bat',
        'justin',
        'knight',
        'jan',
        'monk',
        'sorcerer',
        'jack',
        'mark',
        'hunter',
        'bandit',
        'deep',
        'john',
        'henry',
        'rudolf',
        'louis',
        'firen',
        'freeze',
        'dennis',
        'woody',
        'davis',
    }

    filename_chars = []

    # remove 'data.csv' contents
    with open('data.csv', 'w') as f:
        pass

    # get filenames containing the word from the list chars
    for char in chars:
        filenames_containing = [file for file in files if char in file]
        print(filenames_containing[0])
        filename_chars.append(filenames_containing[0])

    # get a character for columns
    bmp_lines = get_bmp_lines(filename_chars[0])
    values = get_values(bmp_lines)

    # csv columns are first elements of values
    with open('data.csv', 'a') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(values.keys())

    # create a csv with the values for each character
    for filename in filename_chars:
        bmp_lines = get_bmp_lines(filename)
        values = get_values(bmp_lines)
        with open('data.csv', 'a') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(values.values())

    # remove empty lines from data.csv and overwrite it
    with open('data.csv', 'r') as f:
        lines = f.readlines()
    with open('data.csv', 'w') as f:
        for line in lines:
            if line.strip():
                # replace : with none
                line = line.replace(':', '')
                line = line.replace(',', '\t')
                f.write(line)
