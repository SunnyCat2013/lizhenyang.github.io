# pandas 中的 DataFrame

1. 去重

```
distinct_file_score = df['final_score'].unique()
```

# Reference

https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html

# join/merge
## merge
```
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
         left_index=False, right_index=False, sort=True,
         suffixes=('_x', '_y'), copy=True, indicator=False,
         validate=None)
```

# loc

```
DataFrame.loc
Access a group of rows and columns by label(s) or a boolean array.

.loc[] is primarily label based, but may also be used with a boolean array.

Allowed inputs are:

A single label, e.g. 5 or 'a', (note that 5 is interpreted as a label of the index, and never as an integer position along the index).

A list or array of labels, e.g. ['a', 'b', 'c'].

A slice object with labels, e.g. 'a':'f'.

Warning Note that contrary to usual python slices, both the start and the stop are included
A boolean array of the same length as the axis being sliced, e.g. [True, False, True].

A callable function with one argument (the calling Series, DataFrame or Panel) and that returns valid output for indexing (one of the above)

See more at Selection by Label

Raises:	
KeyError:

when any items are not found
```





```
import pandas as pd
df = pd.read_csv('some-of-your-csv-file.csv', sep = '\t')

dir(df)

['T',
 '_AXIS_ALIASES',
 '_AXIS_IALIASES',
 '_AXIS_LEN',
 '_AXIS_NAMES',
 '_AXIS_NUMBERS',
 '_AXIS_ORDERS',
 '_AXIS_REVERSED',
 '_AXIS_SLICEMAP',
 '__abs__',
 '__add__',
 '__and__',
 '__array__',
 '__array_wrap__',
 '__bool__',
 '__bytes__',
 '__class__',
 '__contains__',
 '__copy__',
 '__deepcopy__',
 '__delattr__',
 '__delitem__',
 '__dict__',
 '__dir__',
 '__div__',
 '__doc__',
 '__eq__',
 '__finalize__',
 '__floordiv__',
 '__format__',
 '__ge__',
 '__getattr__',
 '__getattribute__',
 '__getitem__',
 '__getstate__',
 '__gt__',
 '__hash__',
 '__iadd__',
 '__iand__',
 '__ifloordiv__',
 '__imod__',
 '__imul__',
 '__init__',
 '__init_subclass__',
 '__invert__',
 '__ior__',
 '__ipow__',
 '__isub__',
 '__iter__',
 '__itruediv__',
 '__ixor__',
 '__le__',
 '__len__',
 '__lt__',
 '__matmul__',
 '__mod__',
 '__module__',
 '__mul__',
 '__ne__',
 '__neg__',
 '__new__',
 '__nonzero__',
 '__or__',
 '__pos__',
 '__pow__',
 '__radd__',
 '__rand__',
 '__rdiv__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__rfloordiv__',
 '__rmatmul__',
 '__rmod__',
 '__rmul__',
 '__ror__',
 '__round__',
 '__rpow__',
 '__rsub__',
 '__rtruediv__',
 '__rxor__',
 '__setattr__',
 '__setitem__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__sub__',
 '__subclasshook__',
 '__truediv__',
 '__unicode__',
 '__weakref__',
 '__xor__',
 '_accessors',
 '_add_numeric_operations',
 '_add_series_only_operations',
 '_add_series_or_dataframe_operations',
 '_agg_by_level',
 '_agg_doc',
 '_aggregate',
 '_aggregate_multiple_funcs',
 '_align_frame',
 '_align_series',
 '_box_col_values',
 '_box_item_values',
 '_builtin_table',
 '_check_inplace_setting',
 '_check_is_chained_assignment_possible',
 '_check_label_or_level_ambiguity',
 '_check_percentile',
 '_check_setitem_copy',
 '_clear_item_cache',
 '_clip_with_one_bound',
 '_clip_with_scalar',
 '_combine_const',
 '_combine_frame',
 '_combine_match_columns',
 '_combine_match_index',
 '_compare_frame',
 '_consolidate',
 '_consolidate_inplace',
 '_construct_axes_dict',
 '_construct_axes_dict_for_slice',
 '_construct_axes_dict_from',
 '_construct_axes_from_arguments',
 '_constructor',
 '_constructor_expanddim',
 '_constructor_sliced',
 '_convert',
 '_count_level',
 '_create_indexer',
 '_cython_table',
 '_deprecations',
 '_dir_additions',
 '_dir_deletions',
 '_drop_axis',
 '_drop_labels_or_levels',
 '_ensure_valid_index',
 '_expand_axes',
 '_find_valid_index',
 '_from_arrays',
 '_from_axes',
 '_get_agg_axis',
 '_get_axis',
 '_get_axis_name',
 '_get_axis_number',
 '_get_axis_resolvers',
 '_get_block_manager_axis',
 '_get_bool_data',
 '_get_cacher',
 '_get_index_resolvers',
 '_get_item_cache',
 '_get_label_or_level_values',
 '_get_numeric_data',
 '_get_value',
 '_get_values',
 '_getitem_array',
 '_getitem_column',
 '_getitem_frame',
 '_getitem_multilevel',
 '_getitem_slice',
 '_gotitem',
 '_iget_item_cache',
 '_indexed_same',
 '_info_axis',
 '_info_axis_name',
 '_info_axis_number',
 '_info_repr',
 '_init_dict',
 '_init_mgr',
 '_init_ndarray',
 '_internal_names',
 '_internal_names_set',
 '_is_builtin_func',
 '_is_cached',
 '_is_copy',
 '_is_cython_func',
 '_is_datelike_mixed_type',
 '_is_label_or_level_reference',
 '_is_label_reference',
 '_is_level_reference',
 '_is_mixed_type',
 '_is_numeric_mixed_type',
 '_is_view',
 '_ix',
 '_ixs',
 '_join_compat',
 '_maybe_cache_changed',
 '_maybe_update_cacher',
 '_metadata',
 '_needs_reindex_multi',
 '_obj_with_exclusions',
 '_protect_consolidate',
 '_reduce',
 '_reindex_axes',
 '_reindex_axis',
 '_reindex_columns',
 '_reindex_index',
 '_reindex_multi',
 '_reindex_with_indexers',
 '_repr_data_resource_',
 '_repr_fits_horizontal_',
 '_repr_fits_vertical_',
 '_repr_html_',
 '_repr_latex_',
 '_reset_cache',
 '_reset_cacher',
 '_sanitize_column',
 '_selected_obj',
 '_selection',
 '_selection_list',
 '_selection_name',
 '_series',
 '_set_as_cached',
 '_set_axis',
 '_set_axis_name',
 '_set_is_copy',
 '_set_item',
 '_set_value',
 '_setitem_array',
 '_setitem_frame',
 '_setitem_slice',
 '_setup_axes',
 '_shallow_copy',
 '_slice',
 '_stat_axis',
 '_stat_axis_name',
 '_stat_axis_number',
 '_take',
 '_to_dict_of_blocks',
 '_try_aggregate_string_function',
 '_typ',
 '_unpickle_frame_compat',
 '_unpickle_matrix_compat',
 '_update_inplace',
 '_validate_dtype',
 '_values',
 '_where',
 '_xs',
 'abs',
 'add',
 'add_prefix',
 'add_suffix',
 'agg',
 'aggregate',
 'align',
 'all',
 'any',
 'api_type',
 'append',
 'apply',
 'applymap',
 'as_matrix',
 'asfreq',
 'asof',
 'assign',
 'astype',
 'at',
 'at_time',
 'axes',
 'between_time',
 'bfill',
 'bool',
 'boxplot',
 'brand_code',
 'cat_1',
 'cat_1_name',
 'cat_2',
 'cat_2_name',
 'cat_3',
 'cat_3_name',
 'clip',
 'clip_lower',
 'clip_upper',
 'columns',
 'combine',
 'combine_first',
 'compound',
 'copy',
 'corr',
 'corrwith',
 'count',
 'cov',
 'cummax',
 'cummin',
 'cumprod',
 'cumsum',
 'describe',
 'diff',
 'div',
 'divide',
 'dot',
 'drop',
 'drop_duplicates',
 'dropna',
 'dt',
 'dtypes',
 'duplicated',
 'dv',
 'empty',
 'eq',
 'equals',
 'eval',
 'ewm',
 'expanding',
 'ffill',
 'fillna',
 'filter',
 'final_score',
 'first',
 'first_valid_index',
 'floordiv',
 'from_dict',
 'from_records',
 'ftypes',
 'ge',
 'get',
 'get_dtype_counts',
 'get_ftype_counts',
 'get_values',
 'groupby',
 'gt',
 'head',
 'hist',
 'iat',
 'idxmax',
 'idxmin',
 'iloc',
 'image_key',
 'image_path',
 'image_type',
 'index',
 'infer_objects',
 'info',
 'insert',
 'interpolate',
 'isin',
 'isna',
 'isnull',
 'item_id',
 'item_score',
 'item_sku_id',
 'items',
 'iteritems',
 'iterrows',
 'itertuples',
 'ix',
 'join',
 'keys',
 'kurt',
 'kurtosis',
 'last',
 'last_valid_index',
 'le',
 'loc',
 'lookup',
 'lt',
 'mad',
 'mask',
 'max',
 'mean',
 'median',
 'melt',
 'memory_usage',
 'merge',
 'min',
 'mod',
 'mode',
 'mul',
 'multiply',
 'ndim',
 'ne',
 'nlargest',
 'notna',
 'notnull',
 'nsmallest',
 'nunique',
 'pct_change',
 'pipe',
 'pivot',
 'pivot_table',
 'plot',
 'pop',
 'pow',
 'prod',
 'product',
 'quantile',
 'query',
 'radd',
 'rank',
 'rdiv',
 'reindex',
 'reindex_axis',
 'reindex_like',
 'rename',
 'rename_axis',
 'reorder_levels',
 'replace',
 'resample',
 'reset_index',
 'rfloordiv',
 'rmod',
 'rmul',
 'rolling',
 'round',
 'rpow',
 'rsub',
 'rtruediv',
 'sample',
 'sample_cnt',
 'score',
 'score_max',
 'score_means',
 'score_min',
 'score_stddev',
 'select',
 'select_dtypes',
 'sem',
 'set_axis',
 'set_index',
 'shape',
 'shift',
 'shop_name',
 'size',
 'skew',
 'slice_shift',
 'sort_index',
 'sort_values',
 'squeeze',
 'stack',
 'std',
 'style',
 'sub',
 'subtract',
 'sum',
 'swapaxes',
 'swaplevel',
 'tail',
 'take',
 'to_clipboard',
 'to_csv',
 'to_dense',
 'to_dict',
 'to_excel',
 'to_feather',
 'to_gbq',
 'to_hdf',
 'to_html',
 'to_json',
 'to_latex',
 'to_msgpack',
 'to_panel',
 'to_parquet',
 'to_period',
 'to_pickle',
 'to_records',
 'to_sparse',
 'to_sql',
 'to_stata',
 'to_string',
 'to_timestamp',
 'to_xarray',
 'transform',
 'transpose',
 'truediv',
 'truncate',
 'tshift',
 'tz_convert',
 'tz_localize',
 'unstack',
 'update',
 'values',
 'var',
 'vendor_id',
 'where',
 'xs']
 ```
