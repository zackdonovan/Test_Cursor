import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons

class FourierSeriesVisualizer:
    def __init__(self):
        self.fig, self.ax = plt.subplots(figsize=(12, 8))
        plt.subplots_adjust(left=0.1, bottom=0.25, right=0.9, top=0.9)
        
        # Initialize parameters
        self.num_terms = 5
        self.frequency = 1.0
        self.amplitude = 1.0
        self.current_function = 'square'
        
        # Create x-axis
        self.x = np.linspace(-2*np.pi, 2*np.pi, 1000)
        
        # Initialize plot
        self.line, = self.ax.plot(self.x, self.calculate_fourier_series(), 'b-', linewidth=2, label='Fourier Series')
        self.ax.set_xlim(-2*np.pi, 2*np.pi)
        self.ax.set_ylim(-2, 2)
        self.ax.grid(True, alpha=0.3)
        self.ax.set_xlabel('x')
        self.ax.set_ylabel('f(x)')
        self.ax.set_title('Fourier Series Visualizer')
        self.ax.legend()
        
        # Add sliders
        self.add_sliders()
        
        # Add buttons
        self.add_buttons()
        
        # Add radio buttons for different functions
        self.add_radio_buttons()
        
        self.update_plot()
        
    def square_wave(self, x, n_terms):
        """Calculate square wave Fourier series"""
        result = np.zeros_like(x)
        for n in range(1, n_terms + 1, 2):  # Only odd terms
            result += (4 / (n * np.pi)) * np.sin(n * self.frequency * x)
        return result
    
    def sawtooth_wave(self, x, n_terms):
        """Calculate sawtooth wave Fourier series"""
        result = np.zeros_like(x)
        for n in range(1, n_terms + 1):
            result += (2 / (n * np.pi)) * (-1)**(n+1) * np.sin(n * self.frequency * x)
        return result
    
    def triangle_wave(self, x, n_terms):
        """Calculate triangle wave Fourier series"""
        result = np.zeros_like(x)
        for n in range(1, n_terms + 1, 2):  # Only odd terms
            result += (8 / (n**2 * np.pi**2)) * (-1)**((n-1)/2) * np.sin(n * self.frequency * x)
        return result
    
    def pulse_wave(self, x, n_terms):
        """Calculate pulse wave Fourier series (rectangular pulse)"""
        result = np.zeros_like(x)
        for n in range(1, n_terms + 1):
            result += (2 / (n * np.pi)) * np.sin(n * np.pi / 2) * np.cos(n * self.frequency * x)
        return result
    
    def calculate_fourier_series(self):
        """Calculate the Fourier series based on current function"""
        if self.current_function == 'square':
            return self.amplitude * self.square_wave(self.x, self.num_terms)
        elif self.current_function == 'sawtooth':
            return self.amplitude * self.sawtooth_wave(self.x, self.num_terms)
        elif self.current_function == 'triangle':
            return self.amplitude * self.triangle_wave(self.x, self.num_terms)
        elif self.current_function == 'pulse':
            return self.amplitude * self.pulse_wave(self.x, self.num_terms)
        else:
            return np.zeros_like(self.x)
    
    def add_sliders(self):
        """Add interactive sliders"""
        # Terms slider
        ax_terms = plt.axes([0.1, 0.15, 0.3, 0.03])
        self.slider_terms = Slider(ax_terms, 'Terms', 1, 20, valinit=self.num_terms, valstep=1)
        self.slider_terms.on_changed(self.update_terms)
        
        # Frequency slider
        ax_freq = plt.axes([0.1, 0.10, 0.3, 0.03])
        self.slider_freq = Slider(ax_freq, 'Frequency', 0.1, 5.0, valinit=self.frequency)
        self.slider_freq.on_changed(self.update_frequency)
        
        # Amplitude slider
        ax_amp = plt.axes([0.1, 0.05, 0.3, 0.03])
        self.slider_amp = Slider(ax_amp, 'Amplitude', 0.1, 3.0, valinit=self.amplitude)
        self.slider_amp.on_changed(self.update_amplitude)
    
    def add_buttons(self):
        """Add control buttons"""
        # Populate button
        ax_populate = plt.axes([0.6, 0.15, 0.1, 0.04])
        self.btn_populate = Button(ax_populate, 'Populate')
        self.btn_populate.on_clicked(self.populate_series)
        
        # Reset button
        ax_reset = plt.axes([0.75, 0.15, 0.1, 0.04])
        self.btn_reset = Button(ax_reset, 'Reset')
        self.btn_reset.on_clicked(self.reset)
    
    def add_radio_buttons(self):
        """Add radio buttons for function selection"""
        ax_radio = plt.axes([0.6, 0.05, 0.2, 0.08])
        self.radio = RadioButtons(ax_radio, ('square', 'sawtooth', 'triangle', 'pulse'),
                                 active=0)
        self.radio.on_clicked(self.update_function)
    
    def update_terms(self, val):
        """Update number of terms"""
        self.num_terms = int(val)
        self.update_plot()
    
    def update_frequency(self, val):
        """Update frequency"""
        self.frequency = val
        self.update_plot()
    
    def update_amplitude(self, val):
        """Update amplitude"""
        self.amplitude = val
        self.update_plot()
    
    def update_function(self, label):
        """Update the function type"""
        self.current_function = label
        self.update_plot()
    
    def update_plot(self):
        """Update the plot with new data"""
        y = self.calculate_fourier_series()
        self.line.set_ydata(y)
        self.ax.set_title(f'Fourier Series: {self.current_function.capitalize()} Wave ({self.num_terms} terms)')
        self.fig.canvas.draw_idle()
    
    def populate_series(self, event):
        """Populate the series with the current number of terms"""
        self.update_plot()
        print(f"Fourier series populated with {self.num_terms} terms")
    
    def reset(self, event):
        """Reset all parameters to default"""
        self.slider_terms.set_val(5)
        self.slider_freq.set_val(1.0)
        self.slider_amp.set_val(1.0)
        self.radio.set_active(0)
        self.update_plot()
    
    def show(self):
        """Show the plot"""
        plt.show()

def main():
    """Main function to run the visualizer"""
    print("Fourier Series Visualizer")
    print("Controls:")
    print("- Use sliders to adjust terms, frequency, and amplitude")
    print("- Use radio buttons to select different wave types")
    print("- Click 'Populate' to populate the series")
    print("- Click 'Reset' to return to default values")
    print()
    
    visualizer = FourierSeriesVisualizer()
    visualizer.show()

if __name__ == "__main__":
    main()
