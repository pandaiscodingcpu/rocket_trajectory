import numpy as np
import matplotlib.pyplot as plt

class Rocket:
    def __init__(self, A, T, M, m, burn_rate, t):
        self.a = A
        self.t = t
        self.M = M
        self.m = m
        self.br = burn_rate
        self.T = T

    def take_inpts(self):
        print("\nEnter the below Parameters for rocket:\n1. Area of Cross-Section(A)\n2. Initial Thrust\n3. Initial Mass of the rocket\n4. Fuel Mass"
              "\n5. Burn rate of fuel\n6. Total Time of flight\n")
        self.a = float(input("A: "))
        self.T = float(input("Initial Thrust: "))
        self.M = float(input("Initial Mass: "))
        self.m = float(input("Fuel Mass: "))
        self.br = float(input("Burn Rate: "))
        self.t = float(input("Total Time: "))

    def actual_calculation(self):
        constants = {
            'g': 9.81,
            'cd': 0.5,
            'rho': 1.225,
            'dt': 0.1
        }
        v, h = 0, 0
        mass = self.M + self.m  # Initial total mass
        time = [0]
        altitude = [h]
        velocity = [v]
        t = 0

        while t < self.t:
            drag = (0.5 * constants['cd'] * constants['rho'] * self.a * v**2) * np.sign(v)

            if self.m > 0:
                T = self.T
                self.m -= self.br * constants['dt']
                mass -= self.br * constants['dt']  # ✅ Corrected mass reduction
            else:
                T = 0

            a = (T - (mass * constants['g'])) / mass  # ✅ Fixed acceleration formula
            v += a * constants['dt']
            h += v * constants['dt']

            if h < 0:  # Rocket has landed
                break

            velocity.append(v)
            time.append(t)
            altitude.append(h)

            t += constants['dt']  # ✅ Update time correctly

        # Plot results
        def plot(time, alt):
            plt.figure(figsize=(10, 5))
            plt.plot(time, alt, label="Altitude (m)", color="green")
            plt.xlabel('Time (s)')
            plt.ylabel('Altitude (m)')
            plt.grid()
            plt.legend()
            plt.show()

        plot(time, altitude)

# Run the simulation
print("\t\tWELCOME TO ROCKET SIMULATION MODULE\t\t")
r = Rocket(0, 0, 0, 0, 0, 0)
r.take_inpts()
r.actual_calculation()
