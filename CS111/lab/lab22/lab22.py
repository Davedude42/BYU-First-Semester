import matplotlib.pyplot as plt

def plot_histogram():
    with open('admission_algorithms_dataset.csv', 'r') as file:
        lines = file.readlines()
        students = [line.split(',') for line in lines][1:]

        sats = [float(student[1]) for student in students]
        gpas = [float(student[2]) for student in students]
      
        plt.hist(sats)
        plt.savefig("sat_score.png")
        plt.clf()
        plt.hist(gpas)
        plt.savefig("gpa.png")
        plt.clf()



def plot_scatter():
    with open('admission_algorithms_dataset.csv', 'r') as file:
        lines = file.readlines()
        students = [line.split(',') for line in lines][1:]

        sats = [float(student[1]) for student in students]
        gpas = [float(student[2]) for student in students]
      
        plt.scatter(gpas, sats)
        plt.savefig("correlation.png")
        plt.clf()


def plot_spectra():
    with open('spectrum1.txt', 'r') as file1:
        with open('spectrum2.txt', 'r') as file2:
            spectra1 = [line.split('   ') for line in file1.readlines()]
            spectra2 = [line.split('   ') for line in file2.readlines()]

            wavelength1 = [float(spectrum[0]) for spectrum in spectra1]
            flux1 = [float(spectrum[1]) for spectrum in spectra1]

            wavelength2 = [float(spectrum[0]) for spectrum in spectra2]
            flux2 = [float(spectrum[1]) for spectrum in spectra2]
        
            plt.plot(wavelength1, flux1, 'b')
            plt.plot(wavelength2, flux2, 'g')
            plt.savefig("spectra.png")
            plt.clf()



def main():
    # plot_histogram()
    # plot_scatter()
    plot_spectra()


if __name__ == "__main__":
    main()
