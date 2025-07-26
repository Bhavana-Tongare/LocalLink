from flask import Flask, render_template, redirect, url_for, request, session, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# Dummy user credentials for demo (for real app, use a database)
USERS = {
    'supplier': {'email': 'supplier@gmail.com', 'password': 'pass123'},
    'vendor': {'email': 'vendor@gmail.com', 'password': 'pass456'}
}

# ✅ Home page
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/supplier/login', methods=['GET', 'POST'])
def supplier_login():
    if request.method == 'POST':
        email = request.form['email']  # ✅ corrected
        password = request.form['password']
        if email == USERS['supplier']['email'] and password == USERS['supplier']['password']:
            session['user_role'] = 'supplier'
            flash('Logged in as Supplier!', 'success')
            return redirect(url_for('supplier_dashboard'))
        else:
            flash('Invalid credentials for supplier.', 'danger')
    return render_template('supplier_login.html')


# ✅ Vendor Login
@app.route('/vendor/login', methods=['GET', 'POST'])
def vendor_login():
    if request.method == 'POST':
        email = request.form['email']  # ✅ corrected
        password = request.form['password']
        if email == USERS['vendor']['email'] and password == USERS['vendor']['password']:
            session['user_role'] = 'vendor'
            flash('Logged in as Vendor!', 'success')
            return redirect(url_for('vendor_dashboard'))
        else:
            flash('Invalid credentials for vendor.', 'danger')
    return render_template('vendor_login.html')


# ✅ Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']
        role = request.form['role']

        # Just a placeholder: You can save these details in a database
        flash(f'Registration successful for {role.capitalize()} ({name})! You can now log in.', 'success')
        if role == 'supplier':
            return redirect(url_for('supplier_login'))
        else:
            return redirect(url_for('vendor_login'))

    return render_template('register.html')

# ✅ Supplier Dashboard
@app.route('/supplier')
def supplier_dashboard():
    if session.get('user_role') == 'supplier':
        return render_template('supplier.html')
    flash('Please log in as Supplier to access this page.', 'warning')
    return redirect(url_for('supplier_login'))

# ✅ Vendor Dashboard
@app.route('/vendor')
def vendor_dashboard():
    if session.get('user_role') == 'vendor':
        return render_template('vendor.html')
    flash('Please log in as Vendor to access this page.', 'warning')
    return redirect(url_for('vendor_login'))

@app.route('/about')
def about():
    return render_template('about_us.html')

@app.route('/features')
def features():
    return render_template('features.html')

# ✅ Logout
@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
