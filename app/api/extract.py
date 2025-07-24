from flask_restful import Resource
from flask import request

import pandas as pd
import mimetypes

class ExtractionAPI(Resource):
    def post(self):
        input = request.files.get('input')

        if not input.mimetype:
            return 'Cannot identify file type.', 400
        
        ext = mimetypes.guess_extension(input.mimetype)

        if not ext:
            return 'Cannot identify file type.', 400
        
        if not ext in ('.xlsx', '.csv'):
            return 'Only XLSX and CSV files are supported.'
        
        if ext == '.xlsx':
            df = pd.read_excel(input.stream)
        else:
            df = pd.read_csv(input.stream)

        fields = []
        for i in range(df.shape[1]):
            col, dtype = df.columns[i], df.dtypes.iloc[i]

            if pd.api.types.is_bool_dtype(dtype):
                fields.append({'label': col, 'type': 'radio'})
            elif pd.api.types.is_numeric_dtype(dtype):
                fields.append({'label': col, 'type': 'number'})
            elif pd.api.types.is_datetime64_dtype(dtype):
                fields.append({'label': col, 'type': 'date'})
            else:
                fields.append({'label': col, 'type': 'text'})
                
        return fields
