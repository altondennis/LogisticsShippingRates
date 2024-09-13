# Shipping Cost Calculator

## Input package weight and shipping rate
Weight = float(input("Enter the package weight in kilograms: "))
Rate = float(input("Enter the shipping rate per kilogram: "))

## Calculate shipping cost
Shipping_Cost = Weight * Rate

## Display the result
Print(f"Shipping Cost: {shipping_cost} USD")
