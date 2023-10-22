from flask import Flask, jsonify, request 
from flask_restful import Api 
import eco

app = Flask(__name__) 
api = Api(app) 

## REGIONS
@app.route('/regions')
def getRegions():
    regions = list(eco.benefits.regions)
    return jsonify({'regions': regions }) 

## FACTORS
@app.route('/factors', methods=['POST'])
def getFactors():
    region = request.json.get('region')
    factors = list(eco.benefits.factors_for_region(region))
    return jsonify({'factors': factors }) 

## ELECTRICITY BENEFIT
@app.route('/electricity', methods=['POST'])
def getElectricityBenefit():
    
    region = request.json.get('region')
    genus = request.json.get('genus')
    specie = request.json.get('species')
    dbh_cm = request.json.get('dbh_cm')

    species_code = eco.benefits.lookup_species_code(region, genus, specie)
    kwh_saved = eco.benefits.get_energy_conserved(region, [(species_code, dbh_cm)])
    return jsonify({'kwh_saved': kwh_saved })

## STORMWATER BENEFIT
@app.route('/stormwater', methods=['POST'])
def getStormwaterBenefit():
    
    region = request.json.get('region')
    genus = request.json.get('genus')
    specie = request.json.get('species')
    dbh_cm = request.json.get('dbh_cm')

    species_code = eco.benefits.lookup_species_code(region, genus, specie)
    stormwater = eco.benefits.get_stormwater_management(region, [(species_code, dbh_cm)])
    return jsonify({'stormwater': stormwater })

## AIRQUALITY BENEFIT
@app.route('/airquality', methods=['POST'])
def getAirQualityBenefit():
    
    region = request.json.get('region')
    genus = request.json.get('genus')
    specie = request.json.get('species')
    dbh_cm = request.json.get('dbh_cm')

    species_code = eco.benefits.lookup_species_code(region, genus, specie)
    air_quality = eco.benefits.get_air_quality_stats(region, [(species_code, dbh_cm)])
    return jsonify({'airquality': air_quality })

## C02 BENEFIT
@app.route('/c02stats', methods=['POST'])
def getCo2StatsBenefit():
    
    region = request.json.get('region')
    genus = request.json.get('genus')
    specie = request.json.get('species')
    dbh_cm = request.json.get('dbh_cm')

    species_code = eco.benefits.lookup_species_code(region, genus, specie)
    c02_stats = eco.benefits.get_co2_stats(region, [(species_code, dbh_cm)])
    return jsonify({'CO2_stats': c02_stats })

if __name__ == '__main__': 
    app.run(debug = True) 