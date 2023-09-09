from install_requirements import install_requirements
print("Do you want to install the requirements? (y/n)")
if input() == "y":
    print("Installing requirements...")
    install_requirements()
    print("Requirements installed.")

from website import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)