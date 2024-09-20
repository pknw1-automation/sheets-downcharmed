#!/bin/bash
rm web/templates/rendered/*.html 

flask run --port=5555 --host=0.0.0.0
