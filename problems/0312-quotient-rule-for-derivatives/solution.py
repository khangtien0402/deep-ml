import numpy as np


def quotient_rule_derivative(
    g_coeffs: list[float], h_coeffs: list[float], x: float
) -> float:
  # Tính đạo hàm của đa thức g(x) và h(x)
  g_prime_coeffs = np.polyder(g_coeffs)
  h_prime_coeffs = np.polyder(h_coeffs)

  # Tính giá trị của g(x), h(x), g'(x), h'(x) tại điểm x
  g_val = np.polyval(g_coeffs, x)
  h_val = np.polyval(h_coeffs, x)
  g_prime_val = np.polyval(g_prime_coeffs, x)
  h_prime_val = np.polyval(h_prime_coeffs, x)

  # Áp dụng công thức (g'h - gh') / h^2
  result = (g_prime_val * h_val - g_val * h_prime_val) / (h_val**2)
  return float(result)