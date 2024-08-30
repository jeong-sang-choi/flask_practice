from flask import Flask, jsonify, request, render_template
from flask_login import LoginManager, current_user, login_required, login_user, logout_user
from flask_cors import 
import os