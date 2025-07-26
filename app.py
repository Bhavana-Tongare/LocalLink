from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Main Index Page
@app.route('/')
def index():
    return render_template('index.html')  # Main dashboard

# Supplier Dashboard
@app.route('/supplier')
def supplier_dashboard():
    return render_template('supplier.html')

# Vendor Dashboard
@app.route('/vendor')
def vendor_dashboard():
    return render_template('vendor.html')

# Supplier Profile
@app.route('/supplier/profile')
def supplier_profile():
    return "<h2>Supplier Profile Page (Under Construction)</h2>"

# Vendor Profile
@app.route('/vendor/profile')
def vendor_profile():
    return "<h2>Vendor Profile Page (Under Construction)</h2>"

# Supplier Listings
@app.route('/supplier/listings')
def supplier_listings():
    return "<h2>Supplier Listings Page (Under Construction)</h2>"

# Vendor Bids
@app.route('/vendor/bids')
def vendor_bids():
    return "<h2>Vendor Bids Page (Under Construction)</h2>"

# Logout
@app.route('/logout')
def logout():
    return redirect(url_for('index'))

# Run the App
if __name__ == '__main__':
    app.run(debug=True)
