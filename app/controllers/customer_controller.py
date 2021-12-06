from flask import request, jsonify, current_app
import sqlalchemy 
import psycopg2
from sqlalchemy import and_, or_