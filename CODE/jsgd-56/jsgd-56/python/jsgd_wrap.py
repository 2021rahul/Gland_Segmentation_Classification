# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.
# This file is compatible with both classic and new-style classes.

from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_jsgd_wrap', [dirname(__file__)])
        except ImportError:
            import _jsgd_wrap
            return _jsgd_wrap
        if fp is not None:
            try:
                _mod = imp.load_module('_jsgd_wrap', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _jsgd_wrap = swig_import_helper()
    del swig_import_helper
else:
    import _jsgd_wrap
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static) or hasattr(self,name):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


def _frompointer_and_acquire(aclass,ptr):
  r=aclass.frompointer(ptr)
  if r: r.this.acquire()
  return r

class fvec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, fvec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, fvec, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _jsgd_wrap.new_fvec(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _jsgd_wrap.delete_fvec
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _jsgd_wrap.fvec___getitem__(self, *args)
    def __setitem__(self, *args): return _jsgd_wrap.fvec___setitem__(self, *args)
    def cast(self): return _jsgd_wrap.fvec_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _jsgd_wrap.fvec_frompointer
    if _newclass:frompointer = staticmethod(_jsgd_wrap.fvec_frompointer)
    def plus(self, *args): return _jsgd_wrap.fvec_plus(self, *args)
    def clear(self, *args): return _jsgd_wrap.fvec_clear(self, *args)
    def copyfrom(self, *args): return _jsgd_wrap.fvec_copyfrom(self, *args)
    def tostring(self, *args): return _jsgd_wrap.fvec_tostring(self, *args)
    def fromstring(self, *args): return _jsgd_wrap.fvec_fromstring(self, *args)
fvec_swigregister = _jsgd_wrap.fvec_swigregister
fvec_swigregister(fvec)

def fvec_frompointer(*args):
  return _jsgd_wrap.fvec_frompointer(*args)
fvec_frompointer = _jsgd_wrap.fvec_frompointer

fvec.aptr=fvec.acquirepointer=staticmethod(lambda ptr: _frompointer_and_acquire(fvec,ptr))

class ivec(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ivec, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ivec, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _jsgd_wrap.new_ivec(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _jsgd_wrap.delete_ivec
    __del__ = lambda self : None;
    def __getitem__(self, *args): return _jsgd_wrap.ivec___getitem__(self, *args)
    def __setitem__(self, *args): return _jsgd_wrap.ivec___setitem__(self, *args)
    def cast(self): return _jsgd_wrap.ivec_cast(self)
    __swig_getmethods__["frompointer"] = lambda x: _jsgd_wrap.ivec_frompointer
    if _newclass:frompointer = staticmethod(_jsgd_wrap.ivec_frompointer)
    def plus(self, *args): return _jsgd_wrap.ivec_plus(self, *args)
    def clear(self, *args): return _jsgd_wrap.ivec_clear(self, *args)
    def copyfrom(self, *args): return _jsgd_wrap.ivec_copyfrom(self, *args)
    def tostring(self, *args): return _jsgd_wrap.ivec_tostring(self, *args)
    def fromstring(self, *args): return _jsgd_wrap.ivec_fromstring(self, *args)
ivec_swigregister = _jsgd_wrap.ivec_swigregister
ivec_swigregister(ivec)

def ivec_frompointer(*args):
  return _jsgd_wrap.ivec_frompointer(*args)
ivec_frompointer = _jsgd_wrap.ivec_frompointer

ivec.aptr=ivec.acquirepointer=staticmethod(lambda ptr: _frompointer_and_acquire(ivec,ptr))


def bvec_to_numpy(*args):
  return _jsgd_wrap.bvec_to_numpy(*args)
bvec_to_numpy = _jsgd_wrap.bvec_to_numpy

def bvec_to_numpy_ref(*args):
  return _jsgd_wrap.bvec_to_numpy_ref(*args)
bvec_to_numpy_ref = _jsgd_wrap.bvec_to_numpy_ref

def numpy_to_bvec(*args):
  return _jsgd_wrap.numpy_to_bvec(*args)
numpy_to_bvec = _jsgd_wrap.numpy_to_bvec

def numpy_to_bvec_ref(*args):
  return _jsgd_wrap.numpy_to_bvec_ref(*args)
numpy_to_bvec_ref = _jsgd_wrap.numpy_to_bvec_ref

def fvec_to_numpy(*args):
  return _jsgd_wrap.fvec_to_numpy(*args)
fvec_to_numpy = _jsgd_wrap.fvec_to_numpy

def fvec_to_numpy_ref(*args):
  return _jsgd_wrap.fvec_to_numpy_ref(*args)
fvec_to_numpy_ref = _jsgd_wrap.fvec_to_numpy_ref

def numpy_to_fvec(*args):
  return _jsgd_wrap.numpy_to_fvec(*args)
numpy_to_fvec = _jsgd_wrap.numpy_to_fvec

def numpy_to_fvec_ref(*args):
  return _jsgd_wrap.numpy_to_fvec_ref(*args)
numpy_to_fvec_ref = _jsgd_wrap.numpy_to_fvec_ref

def ivec_to_numpy(*args):
  return _jsgd_wrap.ivec_to_numpy(*args)
ivec_to_numpy = _jsgd_wrap.ivec_to_numpy

def ivec_to_numpy_ref(*args):
  return _jsgd_wrap.ivec_to_numpy_ref(*args)
ivec_to_numpy_ref = _jsgd_wrap.ivec_to_numpy_ref

def numpy_to_ivec(*args):
  return _jsgd_wrap.numpy_to_ivec(*args)
numpy_to_ivec = _jsgd_wrap.numpy_to_ivec

def numpy_to_ivec_ref(*args):
  return _jsgd_wrap.numpy_to_ivec_ref(*args)
numpy_to_ivec_ref = _jsgd_wrap.numpy_to_ivec_ref

def dvec_to_numpy(*args):
  return _jsgd_wrap.dvec_to_numpy(*args)
dvec_to_numpy = _jsgd_wrap.dvec_to_numpy

def dvec_to_numpy_ref(*args):
  return _jsgd_wrap.dvec_to_numpy_ref(*args)
dvec_to_numpy_ref = _jsgd_wrap.dvec_to_numpy_ref

def numpy_to_dvec(*args):
  return _jsgd_wrap.numpy_to_dvec(*args)
numpy_to_dvec = _jsgd_wrap.numpy_to_dvec

def numpy_to_dvec_ref(*args):
  return _jsgd_wrap.numpy_to_dvec_ref(*args)
numpy_to_dvec_ref = _jsgd_wrap.numpy_to_dvec_ref

def callable_to_ptr(*args):
  return _jsgd_wrap.callable_to_ptr(*args)
callable_to_ptr = _jsgd_wrap.callable_to_ptr
class x_matrix_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, x_matrix_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, x_matrix_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["encoding"] = _jsgd_wrap.x_matrix_t_encoding_set
    __swig_getmethods__["encoding"] = _jsgd_wrap.x_matrix_t_encoding_get
    if _newclass:encoding = _swig_property(_jsgd_wrap.x_matrix_t_encoding_get, _jsgd_wrap.x_matrix_t_encoding_set)
    __swig_setmethods__["n"] = _jsgd_wrap.x_matrix_t_n_set
    __swig_getmethods__["n"] = _jsgd_wrap.x_matrix_t_n_get
    if _newclass:n = _swig_property(_jsgd_wrap.x_matrix_t_n_get, _jsgd_wrap.x_matrix_t_n_set)
    __swig_setmethods__["d"] = _jsgd_wrap.x_matrix_t_d_set
    __swig_getmethods__["d"] = _jsgd_wrap.x_matrix_t_d_get
    if _newclass:d = _swig_property(_jsgd_wrap.x_matrix_t_d_get, _jsgd_wrap.x_matrix_t_d_set)
    __swig_setmethods__["data"] = _jsgd_wrap.x_matrix_t_data_set
    __swig_getmethods__["data"] = _jsgd_wrap.x_matrix_t_data_get
    if _newclass:data = _swig_property(_jsgd_wrap.x_matrix_t_data_get, _jsgd_wrap.x_matrix_t_data_set)
    __swig_setmethods__["nsq"] = _jsgd_wrap.x_matrix_t_nsq_set
    __swig_getmethods__["nsq"] = _jsgd_wrap.x_matrix_t_nsq_get
    if _newclass:nsq = _swig_property(_jsgd_wrap.x_matrix_t_nsq_get, _jsgd_wrap.x_matrix_t_nsq_set)
    __swig_setmethods__["centroids"] = _jsgd_wrap.x_matrix_t_centroids_set
    __swig_getmethods__["centroids"] = _jsgd_wrap.x_matrix_t_centroids_get
    if _newclass:centroids = _swig_property(_jsgd_wrap.x_matrix_t_centroids_get, _jsgd_wrap.x_matrix_t_centroids_set)
    __swig_setmethods__["codes"] = _jsgd_wrap.x_matrix_t_codes_set
    __swig_getmethods__["codes"] = _jsgd_wrap.x_matrix_t_codes_get
    if _newclass:codes = _swig_property(_jsgd_wrap.x_matrix_t_codes_get, _jsgd_wrap.x_matrix_t_codes_set)
    __swig_setmethods__["indices"] = _jsgd_wrap.x_matrix_t_indices_set
    __swig_getmethods__["indices"] = _jsgd_wrap.x_matrix_t_indices_get
    if _newclass:indices = _swig_property(_jsgd_wrap.x_matrix_t_indices_get, _jsgd_wrap.x_matrix_t_indices_set)
    __swig_setmethods__["indptr"] = _jsgd_wrap.x_matrix_t_indptr_set
    __swig_getmethods__["indptr"] = _jsgd_wrap.x_matrix_t_indptr_get
    if _newclass:indptr = _swig_property(_jsgd_wrap.x_matrix_t_indptr_get, _jsgd_wrap.x_matrix_t_indptr_set)
    __swig_setmethods__["sparse_data"] = _jsgd_wrap.x_matrix_t_sparse_data_set
    __swig_getmethods__["sparse_data"] = _jsgd_wrap.x_matrix_t_sparse_data_get
    if _newclass:sparse_data = _swig_property(_jsgd_wrap.x_matrix_t_sparse_data_get, _jsgd_wrap.x_matrix_t_sparse_data_set)
    __swig_setmethods__["vector_begin"] = _jsgd_wrap.x_matrix_t_vector_begin_set
    __swig_getmethods__["vector_begin"] = _jsgd_wrap.x_matrix_t_vector_begin_get
    if _newclass:vector_begin = _swig_property(_jsgd_wrap.x_matrix_t_vector_begin_get, _jsgd_wrap.x_matrix_t_vector_begin_set)
    def __init__(self): 
        this = _jsgd_wrap.new_x_matrix_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _jsgd_wrap.delete_x_matrix_t
    __del__ = lambda self : None;
x_matrix_t_swigregister = _jsgd_wrap.x_matrix_t_swigregister
x_matrix_t_swigregister(x_matrix_t)
JSGD_X_FULL = _jsgd_wrap.JSGD_X_FULL
JSGD_X_SPARSE = _jsgd_wrap.JSGD_X_SPARSE
JSGD_X_PQ = _jsgd_wrap.JSGD_X_PQ
JSGD_X_PQ_SPARSE = _jsgd_wrap.JSGD_X_PQ_SPARSE


def vec_scale(*args):
  return _jsgd_wrap.vec_scale(*args)
vec_scale = _jsgd_wrap.vec_scale

def vec_sqnorm(*args):
  return _jsgd_wrap.vec_sqnorm(*args)
vec_sqnorm = _jsgd_wrap.vec_sqnorm

def vec_dotprod(*args):
  return _jsgd_wrap.vec_dotprod(*args)
vec_dotprod = _jsgd_wrap.vec_dotprod

def vec_addto(*args):
  return _jsgd_wrap.vec_addto(*args)
vec_addto = _jsgd_wrap.vec_addto

def x_matrix_get(*args):
  return _jsgd_wrap.x_matrix_get(*args)
x_matrix_get = _jsgd_wrap.x_matrix_get

def x_matrix_dotprod(*args):
  return _jsgd_wrap.x_matrix_dotprod(*args)
x_matrix_dotprod = _jsgd_wrap.x_matrix_dotprod

def x_matrix_addto(*args):
  return _jsgd_wrap.x_matrix_addto(*args)
x_matrix_addto = _jsgd_wrap.x_matrix_addto

def x_matrix_dotprod_self(*args):
  return _jsgd_wrap.x_matrix_dotprod_self(*args)
x_matrix_dotprod_self = _jsgd_wrap.x_matrix_dotprod_self

def x_matrix_matmul(*args):
  return _jsgd_wrap.x_matrix_matmul(*args)
x_matrix_matmul = _jsgd_wrap.x_matrix_matmul

def x_matrix_matmul_slice(*args):
  return _jsgd_wrap.x_matrix_matmul_slice(*args)
x_matrix_matmul_slice = _jsgd_wrap.x_matrix_matmul_slice

def x_matrix_matmul_thread(*args):
  return _jsgd_wrap.x_matrix_matmul_thread(*args)
x_matrix_matmul_thread = _jsgd_wrap.x_matrix_matmul_thread

def x_matrix_matmul_self(*args):
  return _jsgd_wrap.x_matrix_matmul_self(*args)
x_matrix_matmul_self = _jsgd_wrap.x_matrix_matmul_self
class x_matrix_sparse_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, x_matrix_sparse_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, x_matrix_sparse_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["m"] = _jsgd_wrap.x_matrix_sparse_t_m_set
    __swig_getmethods__["m"] = _jsgd_wrap.x_matrix_sparse_t_m_get
    if _newclass:m = _swig_property(_jsgd_wrap.x_matrix_sparse_t_m_get, _jsgd_wrap.x_matrix_sparse_t_m_set)
    __swig_setmethods__["n"] = _jsgd_wrap.x_matrix_sparse_t_n_set
    __swig_getmethods__["n"] = _jsgd_wrap.x_matrix_sparse_t_n_get
    if _newclass:n = _swig_property(_jsgd_wrap.x_matrix_sparse_t_n_get, _jsgd_wrap.x_matrix_sparse_t_n_set)
    __swig_setmethods__["jc"] = _jsgd_wrap.x_matrix_sparse_t_jc_set
    __swig_getmethods__["jc"] = _jsgd_wrap.x_matrix_sparse_t_jc_get
    if _newclass:jc = _swig_property(_jsgd_wrap.x_matrix_sparse_t_jc_get, _jsgd_wrap.x_matrix_sparse_t_jc_set)
    __swig_setmethods__["ir"] = _jsgd_wrap.x_matrix_sparse_t_ir_set
    __swig_getmethods__["ir"] = _jsgd_wrap.x_matrix_sparse_t_ir_get
    if _newclass:ir = _swig_property(_jsgd_wrap.x_matrix_sparse_t_ir_get, _jsgd_wrap.x_matrix_sparse_t_ir_set)
    __swig_setmethods__["pr"] = _jsgd_wrap.x_matrix_sparse_t_pr_set
    __swig_getmethods__["pr"] = _jsgd_wrap.x_matrix_sparse_t_pr_get
    if _newclass:pr = _swig_property(_jsgd_wrap.x_matrix_sparse_t_pr_get, _jsgd_wrap.x_matrix_sparse_t_pr_set)
    def __init__(self): 
        this = _jsgd_wrap.new_x_matrix_sparse_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _jsgd_wrap.delete_x_matrix_sparse_t
    __del__ = lambda self : None;
x_matrix_sparse_t_swigregister = _jsgd_wrap.x_matrix_sparse_t_swigregister
x_matrix_sparse_t_swigregister(x_matrix_sparse_t)


def x_matrix_sparse_init(*args):
  return _jsgd_wrap.x_matrix_sparse_init(*args)
x_matrix_sparse_init = _jsgd_wrap.x_matrix_sparse_init

def x_matrix_sparse_clear(*args):
  return _jsgd_wrap.x_matrix_sparse_clear(*args)
x_matrix_sparse_clear = _jsgd_wrap.x_matrix_sparse_clear

def x_matrix_matmul_subset(*args):
  return _jsgd_wrap.x_matrix_matmul_subset(*args)
x_matrix_matmul_subset = _jsgd_wrap.x_matrix_matmul_subset

def x_matrix_addto_sparse(*args):
  return _jsgd_wrap.x_matrix_addto_sparse(*args)
x_matrix_addto_sparse = _jsgd_wrap.x_matrix_addto_sparse
class jsgd_params_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, jsgd_params_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, jsgd_params_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["verbose"] = _jsgd_wrap.jsgd_params_t_verbose_set
    __swig_getmethods__["verbose"] = _jsgd_wrap.jsgd_params_t_verbose_get
    if _newclass:verbose = _swig_property(_jsgd_wrap.jsgd_params_t_verbose_get, _jsgd_wrap.jsgd_params_t_verbose_set)
    __swig_setmethods__["n_thread"] = _jsgd_wrap.jsgd_params_t_n_thread_set
    __swig_getmethods__["n_thread"] = _jsgd_wrap.jsgd_params_t_n_thread_get
    if _newclass:n_thread = _swig_property(_jsgd_wrap.jsgd_params_t_n_thread_get, _jsgd_wrap.jsgd_params_t_n_thread_set)
    __swig_setmethods__["random_seed"] = _jsgd_wrap.jsgd_params_t_random_seed_set
    __swig_getmethods__["random_seed"] = _jsgd_wrap.jsgd_params_t_random_seed_get
    if _newclass:random_seed = _swig_property(_jsgd_wrap.jsgd_params_t_random_seed_get, _jsgd_wrap.jsgd_params_t_random_seed_set)
    __swig_setmethods__["use_input_w"] = _jsgd_wrap.jsgd_params_t_use_input_w_set
    __swig_getmethods__["use_input_w"] = _jsgd_wrap.jsgd_params_t_use_input_w_get
    if _newclass:use_input_w = _swig_property(_jsgd_wrap.jsgd_params_t_use_input_w_get, _jsgd_wrap.jsgd_params_t_use_input_w_set)
    __swig_setmethods__["algo"] = _jsgd_wrap.jsgd_params_t_algo_set
    __swig_getmethods__["algo"] = _jsgd_wrap.jsgd_params_t_algo_get
    if _newclass:algo = _swig_property(_jsgd_wrap.jsgd_params_t_algo_get, _jsgd_wrap.jsgd_params_t_algo_set)
    __swig_setmethods__["n_epoch"] = _jsgd_wrap.jsgd_params_t_n_epoch_set
    __swig_getmethods__["n_epoch"] = _jsgd_wrap.jsgd_params_t_n_epoch_get
    if _newclass:n_epoch = _swig_property(_jsgd_wrap.jsgd_params_t_n_epoch_get, _jsgd_wrap.jsgd_params_t_n_epoch_set)
    __swig_setmethods__["valid"] = _jsgd_wrap.jsgd_params_t_valid_set
    __swig_getmethods__["valid"] = _jsgd_wrap.jsgd_params_t_valid_get
    if _newclass:valid = _swig_property(_jsgd_wrap.jsgd_params_t_valid_get, _jsgd_wrap.jsgd_params_t_valid_set)
    __swig_setmethods__["valid_labels"] = _jsgd_wrap.jsgd_params_t_valid_labels_set
    __swig_getmethods__["valid_labels"] = _jsgd_wrap.jsgd_params_t_valid_labels_get
    if _newclass:valid_labels = _swig_property(_jsgd_wrap.jsgd_params_t_valid_labels_get, _jsgd_wrap.jsgd_params_t_valid_labels_set)
    __swig_setmethods__["eval_freq"] = _jsgd_wrap.jsgd_params_t_eval_freq_set
    __swig_getmethods__["eval_freq"] = _jsgd_wrap.jsgd_params_t_eval_freq_get
    if _newclass:eval_freq = _swig_property(_jsgd_wrap.jsgd_params_t_eval_freq_get, _jsgd_wrap.jsgd_params_t_eval_freq_set)
    __swig_setmethods__["compute_train_accuracy"] = _jsgd_wrap.jsgd_params_t_compute_train_accuracy_set
    __swig_getmethods__["compute_train_accuracy"] = _jsgd_wrap.jsgd_params_t_compute_train_accuracy_get
    if _newclass:compute_train_accuracy = _swig_property(_jsgd_wrap.jsgd_params_t_compute_train_accuracy_get, _jsgd_wrap.jsgd_params_t_compute_train_accuracy_set)
    __swig_setmethods__["stop_valid_threshold"] = _jsgd_wrap.jsgd_params_t_stop_valid_threshold_set
    __swig_getmethods__["stop_valid_threshold"] = _jsgd_wrap.jsgd_params_t_stop_valid_threshold_get
    if _newclass:stop_valid_threshold = _swig_property(_jsgd_wrap.jsgd_params_t_stop_valid_threshold_get, _jsgd_wrap.jsgd_params_t_stop_valid_threshold_set)
    __swig_setmethods__["accuracy_function"] = _jsgd_wrap.jsgd_params_t_accuracy_function_set
    __swig_getmethods__["accuracy_function"] = _jsgd_wrap.jsgd_params_t_accuracy_function_get
    if _newclass:accuracy_function = _swig_property(_jsgd_wrap.jsgd_params_t_accuracy_function_get, _jsgd_wrap.jsgd_params_t_accuracy_function_set)
    __swig_setmethods__["accuracy_function_arg"] = _jsgd_wrap.jsgd_params_t_accuracy_function_arg_set
    __swig_getmethods__["accuracy_function_arg"] = _jsgd_wrap.jsgd_params_t_accuracy_function_arg_get
    if _newclass:accuracy_function_arg = _swig_property(_jsgd_wrap.jsgd_params_t_accuracy_function_arg_get, _jsgd_wrap.jsgd_params_t_accuracy_function_arg_set)
    __swig_setmethods__["_lambda"] = _jsgd_wrap.jsgd_params_t__lambda_set
    __swig_getmethods__["_lambda"] = _jsgd_wrap.jsgd_params_t__lambda_get
    if _newclass:_lambda = _swig_property(_jsgd_wrap.jsgd_params_t__lambda_get, _jsgd_wrap.jsgd_params_t__lambda_set)
    __swig_setmethods__["bias_term"] = _jsgd_wrap.jsgd_params_t_bias_term_set
    __swig_getmethods__["bias_term"] = _jsgd_wrap.jsgd_params_t_bias_term_get
    if _newclass:bias_term = _swig_property(_jsgd_wrap.jsgd_params_t_bias_term_get, _jsgd_wrap.jsgd_params_t_bias_term_set)
    __swig_setmethods__["eta0"] = _jsgd_wrap.jsgd_params_t_eta0_set
    __swig_getmethods__["eta0"] = _jsgd_wrap.jsgd_params_t_eta0_get
    if _newclass:eta0 = _swig_property(_jsgd_wrap.jsgd_params_t_eta0_get, _jsgd_wrap.jsgd_params_t_eta0_set)
    __swig_setmethods__["beta"] = _jsgd_wrap.jsgd_params_t_beta_set
    __swig_getmethods__["beta"] = _jsgd_wrap.jsgd_params_t_beta_get
    if _newclass:beta = _swig_property(_jsgd_wrap.jsgd_params_t_beta_get, _jsgd_wrap.jsgd_params_t_beta_set)
    __swig_setmethods__["fixed_eta"] = _jsgd_wrap.jsgd_params_t_fixed_eta_set
    __swig_getmethods__["fixed_eta"] = _jsgd_wrap.jsgd_params_t_fixed_eta_get
    if _newclass:fixed_eta = _swig_property(_jsgd_wrap.jsgd_params_t_fixed_eta_get, _jsgd_wrap.jsgd_params_t_fixed_eta_set)
    __swig_setmethods__["best_epoch"] = _jsgd_wrap.jsgd_params_t_best_epoch_set
    __swig_getmethods__["best_epoch"] = _jsgd_wrap.jsgd_params_t_best_epoch_get
    if _newclass:best_epoch = _swig_property(_jsgd_wrap.jsgd_params_t_best_epoch_get, _jsgd_wrap.jsgd_params_t_best_epoch_set)
    __swig_setmethods__["niter"] = _jsgd_wrap.jsgd_params_t_niter_set
    __swig_getmethods__["niter"] = _jsgd_wrap.jsgd_params_t_niter_get
    if _newclass:niter = _swig_property(_jsgd_wrap.jsgd_params_t_niter_get, _jsgd_wrap.jsgd_params_t_niter_set)
    __swig_setmethods__["ndp"] = _jsgd_wrap.jsgd_params_t_ndp_set
    __swig_getmethods__["ndp"] = _jsgd_wrap.jsgd_params_t_ndp_get
    if _newclass:ndp = _swig_property(_jsgd_wrap.jsgd_params_t_ndp_get, _jsgd_wrap.jsgd_params_t_ndp_set)
    __swig_setmethods__["nmodif"] = _jsgd_wrap.jsgd_params_t_nmodif_set
    __swig_getmethods__["nmodif"] = _jsgd_wrap.jsgd_params_t_nmodif_get
    if _newclass:nmodif = _swig_property(_jsgd_wrap.jsgd_params_t_nmodif_get, _jsgd_wrap.jsgd_params_t_nmodif_set)
    __swig_setmethods__["t_eval"] = _jsgd_wrap.jsgd_params_t_t_eval_set
    __swig_getmethods__["t_eval"] = _jsgd_wrap.jsgd_params_t_t_eval_get
    if _newclass:t_eval = _swig_property(_jsgd_wrap.jsgd_params_t_t_eval_get, _jsgd_wrap.jsgd_params_t_t_eval_set)
    __swig_setmethods__["na_stat_tables"] = _jsgd_wrap.jsgd_params_t_na_stat_tables_set
    __swig_getmethods__["na_stat_tables"] = _jsgd_wrap.jsgd_params_t_na_stat_tables_get
    if _newclass:na_stat_tables = _swig_property(_jsgd_wrap.jsgd_params_t_na_stat_tables_get, _jsgd_wrap.jsgd_params_t_na_stat_tables_set)
    __swig_setmethods__["times"] = _jsgd_wrap.jsgd_params_t_times_set
    __swig_getmethods__["times"] = _jsgd_wrap.jsgd_params_t_times_get
    if _newclass:times = _swig_property(_jsgd_wrap.jsgd_params_t_times_get, _jsgd_wrap.jsgd_params_t_times_set)
    __swig_setmethods__["train_accuracies"] = _jsgd_wrap.jsgd_params_t_train_accuracies_set
    __swig_getmethods__["train_accuracies"] = _jsgd_wrap.jsgd_params_t_train_accuracies_get
    if _newclass:train_accuracies = _swig_property(_jsgd_wrap.jsgd_params_t_train_accuracies_get, _jsgd_wrap.jsgd_params_t_train_accuracies_set)
    __swig_setmethods__["valid_accuracies"] = _jsgd_wrap.jsgd_params_t_valid_accuracies_set
    __swig_getmethods__["valid_accuracies"] = _jsgd_wrap.jsgd_params_t_valid_accuracies_get
    if _newclass:valid_accuracies = _swig_property(_jsgd_wrap.jsgd_params_t_valid_accuracies_get, _jsgd_wrap.jsgd_params_t_valid_accuracies_set)
    __swig_setmethods__["ndotprods"] = _jsgd_wrap.jsgd_params_t_ndotprods_set
    __swig_getmethods__["ndotprods"] = _jsgd_wrap.jsgd_params_t_ndotprods_get
    if _newclass:ndotprods = _swig_property(_jsgd_wrap.jsgd_params_t_ndotprods_get, _jsgd_wrap.jsgd_params_t_ndotprods_set)
    __swig_setmethods__["nmodifs"] = _jsgd_wrap.jsgd_params_t_nmodifs_set
    __swig_getmethods__["nmodifs"] = _jsgd_wrap.jsgd_params_t_nmodifs_get
    if _newclass:nmodifs = _swig_property(_jsgd_wrap.jsgd_params_t_nmodifs_get, _jsgd_wrap.jsgd_params_t_nmodifs_set)
    __swig_setmethods__["best_valid_accuracy"] = _jsgd_wrap.jsgd_params_t_best_valid_accuracy_set
    __swig_getmethods__["best_valid_accuracy"] = _jsgd_wrap.jsgd_params_t_best_valid_accuracy_get
    if _newclass:best_valid_accuracy = _swig_property(_jsgd_wrap.jsgd_params_t_best_valid_accuracy_get, _jsgd_wrap.jsgd_params_t_best_valid_accuracy_set)
    __swig_setmethods__["t0"] = _jsgd_wrap.jsgd_params_t_t0_set
    __swig_getmethods__["t0"] = _jsgd_wrap.jsgd_params_t_t0_get
    if _newclass:t0 = _swig_property(_jsgd_wrap.jsgd_params_t_t0_get, _jsgd_wrap.jsgd_params_t_t0_set)
    __swig_setmethods__["rand_state"] = _jsgd_wrap.jsgd_params_t_rand_state_set
    __swig_getmethods__["rand_state"] = _jsgd_wrap.jsgd_params_t_rand_state_get
    if _newclass:rand_state = _swig_property(_jsgd_wrap.jsgd_params_t_rand_state_get, _jsgd_wrap.jsgd_params_t_rand_state_set)
    __swig_setmethods__["t_block"] = _jsgd_wrap.jsgd_params_t_t_block_set
    __swig_getmethods__["t_block"] = _jsgd_wrap.jsgd_params_t_t_block_get
    if _newclass:t_block = _swig_property(_jsgd_wrap.jsgd_params_t_t_block_get, _jsgd_wrap.jsgd_params_t_t_block_set)
    __swig_setmethods__["n_wstep"] = _jsgd_wrap.jsgd_params_t_n_wstep_set
    __swig_getmethods__["n_wstep"] = _jsgd_wrap.jsgd_params_t_n_wstep_get
    if _newclass:n_wstep = _swig_property(_jsgd_wrap.jsgd_params_t_n_wstep_get, _jsgd_wrap.jsgd_params_t_n_wstep_set)
    __swig_setmethods__["d_step"] = _jsgd_wrap.jsgd_params_t_d_step_set
    __swig_getmethods__["d_step"] = _jsgd_wrap.jsgd_params_t_d_step_get
    if _newclass:d_step = _swig_property(_jsgd_wrap.jsgd_params_t_d_step_get, _jsgd_wrap.jsgd_params_t_d_step_set)
    __swig_setmethods__["self_dotprods"] = _jsgd_wrap.jsgd_params_t_self_dotprods_set
    __swig_getmethods__["self_dotprods"] = _jsgd_wrap.jsgd_params_t_self_dotprods_get
    if _newclass:self_dotprods = _swig_property(_jsgd_wrap.jsgd_params_t_self_dotprods_get, _jsgd_wrap.jsgd_params_t_self_dotprods_set)
    __swig_setmethods__["use_self_dotprods"] = _jsgd_wrap.jsgd_params_t_use_self_dotprods_set
    __swig_getmethods__["use_self_dotprods"] = _jsgd_wrap.jsgd_params_t_use_self_dotprods_get
    if _newclass:use_self_dotprods = _swig_property(_jsgd_wrap.jsgd_params_t_use_self_dotprods_get, _jsgd_wrap.jsgd_params_t_use_self_dotprods_set)
    def __init__(self): 
        this = _jsgd_wrap.new_jsgd_params_t()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _jsgd_wrap.delete_jsgd_params_t
    __del__ = lambda self : None;
jsgd_params_t_swigregister = _jsgd_wrap.jsgd_params_t_swigregister
jsgd_params_t_swigregister(jsgd_params_t)
JSGD_ALGO_OVR = _jsgd_wrap.JSGD_ALGO_OVR
JSGD_ALGO_MUL = _jsgd_wrap.JSGD_ALGO_MUL
JSGD_ALGO_RNK = _jsgd_wrap.JSGD_ALGO_RNK
JSGD_ALGO_WAR = _jsgd_wrap.JSGD_ALGO_WAR


def jsgd_params_set_default(*args):
  return _jsgd_wrap.jsgd_params_set_default(*args)
jsgd_params_set_default = _jsgd_wrap.jsgd_params_set_default

def jsgd_train(*args):
  return _jsgd_wrap.jsgd_train(*args)
jsgd_train = _jsgd_wrap.jsgd_train

def jsgd_compute_scores(*args):
  return _jsgd_wrap.jsgd_compute_scores(*args)
jsgd_compute_scores = _jsgd_wrap.jsgd_compute_scores


