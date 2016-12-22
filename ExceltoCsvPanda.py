import csv
import xlrd
import pandas

def read_excel(io, sheetname=0, header=0, skiprows=None, skip_footer=0,
               index_col=None, names=None, parse_cols=None, parse_dates=False,
               date_parser=None, na_values=None, thousands=None,
               convert_float=True, has_index_names=None, converters=None,
               true_values=None, false_values=None, engine=None, squeeze=False,
               **kwds):

        
	if not isinstance(io, 'Test.xlsx'):  io = 'test.xlsx'(io,engine=engine)
	return io._parse_excel(
        sheetname=sheetname, header=header, skiprows=skiprows, names=names,

                dex_col=index_col, parse_cols=parse_cols, parse_dates=parse_dates,
        date_parser=date_parser, na_values=na_values, thousands=thousands,
        convert_float=convert_float, has_index_names=has_index_names,
        skip_footer=skip_footer, converters=converters,
        true_values=true_values, false_values=false_values, squeeze=squeeze,
        **kwds)

    
def to_csv(self, path_or_buf=None, sep=",", na_rep='', float_format=None,
               columns=None, header=True, index=True, index_label=None,
               mode='w', encoding=None, compression=None, quoting=None,
               quotechar='"', line_terminator='\n', chunksize=None,
               tupleize_cols=False, date_format=None, doublequote=True,
               escapechar=None, decimal='.'):
        
        
 formatter = fmt.CSVFormatter(self, path_or_buf,
                                     line_terminator=line_terminator, sep=sep,
                                     encoding=encoding,
                                     compression=compression, quoting=quoting,
                                     na_rep=na_rep, float_format=float_format,
                                     cols=columns, header=header, index=index,
                                     index_label=index_label, mode=mode,
                                     chunksize=chunksize, quotechar=quotechar,
                                     tupleize_cols=tupleize_cols,
                                     date_format=date_format,
                                     doublequote=doublequote,
                                     escapechar=escapechar, decimal=decimal)

formatter.save()




   
