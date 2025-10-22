from flask import Flask, jsonify, request
import math

app = Flask(__name__)

def compute_factorial(n: int) -> int:
    
    if n < 0:
        raise ValueError("n debe ser entero no negativo")
    if n > 2000:
       
        raise OverflowError("n demasiado grande")
    return math.factorial(n)

def parity_label(x: int) -> str:
    return "par" if (x % 2 == 0) else "impar"

@app.get("/factorial/<int:n>")
def factorial_endpoint(n: int):
    try:
        fact = compute_factorial(n)
        result = {
            "numero": n,
            "factorial": fact,
            "paridad_factorial": parity_label(fact)  
        }
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except OverflowError as oe:
        return jsonify({"error": str(oe)}), 413
    except Exception as e:
        return jsonify({"error": "Error interno"}), 500


@app.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == "__main__":
   
    app.run(host="0.0.0.0", port=8080)
