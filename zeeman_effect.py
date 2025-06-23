# Zeeman Effect Calculator

# Constants
BOHR_MAGNETON = 9.274e-24  # Joules per Tesla

def calculate_zeeman_shift(g_factor, m_j, magnetic_field):
    """
    Calculate the Zeeman effect energy shift.
    Args:
        g_factor (float): Landé g-factor
        m_j (float): Magnetic quantum number
        magnetic_field (float): Magnetic field strength in Tesla
    Returns:
        float: Energy shift in Joules
    """
    return BOHR_MAGNETON * g_factor * m_j * magnetic_field

if __name__ == "__main__":
    print("Zeeman Effect Energy Shift Calculator")
    try:
        g = float(input("Enter Landé g-factor (g): "))
        m_j = float(input("Enter magnetic quantum number (m_j): "))
        B = float(input("Enter magnetic field strength in Tesla (B): "))
        delta_E = calculate_zeeman_shift(g, m_j, B)
        print(f"\nEnergy shift (ΔE): {delta_E:.3e} Joules")
    except ValueError:
        print("Invalid input. Please enter numeric values.") 