def convert_matrices_to_params_dict(model_parameters_dict):
    params_dict = {}

    # pass beta_matrix_l to params_dict
    params_dict["BETAL33"] = model_parameters_dict["beta_matrix_l"][2,2]
    params_dict["BETAL23"] = model_parameters_dict["beta_matrix_l"][1,2]
    params_dict["BETAL32"] = model_parameters_dict["beta_matrix_l"][2,1]

    # pass beta_matrix_r to params_dict
    params_dict["BETARD33"] = model_parameters_dict["beta_matrix_r"][2,2]
    
    # pass zeta_matrix_l to params_dict
    params_dict["ZETAL33"] = model_parameters_dict["zeta_matrix_l"][2,2]
    params_dict["ZETAL23"] = model_parameters_dict["zeta_matrix_l"][1,2]
    params_dict["ZETAL22"] = model_parameters_dict["zeta_matrix_l"][1,1]

    is_hermitian =  model_parameters_dict["zeta_matrix_l"] == model_parameters_dict["zeta_matrix_l"].conj().T
    if not is_hermitian.all():
        raise Exception("zeta_matrix_l is not hermitian")
    
    # pass zeta_matrix_e_r to params_dict
    params_dict["ZETARE33"] = model_parameters_dict["zeta_matrix_e_r"][2,2]
    params_dict["ZETARE22"] = model_parameters_dict["zeta_matrix_e_r"][1,1]

    is_hermitian =  model_parameters_dict["zeta_matrix_e_r"] == model_parameters_dict["zeta_matrix_e_r"].conj().T
    
    if not is_hermitian.all():
        raise Exception("zeta_matrix_e_r is not hermitian")

    # pass zeta_matrix_q_l to params_dict 
    params_dict["ZETAQ33"] = model_parameters_dict["zeta_matrix_q_l"][2,2]
    params_dict["ZETAQLL"] = model_parameters_dict["zeta_matrix_q_l"][1,1]

    is_hermitian =  model_parameters_dict["zeta_matrix_q_l"] == model_parameters_dict["zeta_matrix_q_l"].conj().T

    is_block_diagonal = model_parameters_dict["zeta_matrix_q_l"][1,1] == model_parameters_dict["zeta_matrix_q_l"][0,0]

    if not is_hermitian.all():
        raise Exception("zeta_matrix_q_l is not hermitian")
    elif not is_block_diagonal:
        raise Exception("zeta_matrix_q_l is not block diagonal")
    
    # pass zeta_matrix_u_r to params_dict
    params_dict["ZETARU33"] = model_parameters_dict["zeta_matrix_u_r"][2,2]
    params_dict["ZETARULL"] = model_parameters_dict["zeta_matrix_u_r"][1,1]

    is_hermitian =  model_parameters_dict["zeta_matrix_u_r"] == model_parameters_dict["zeta_matrix_u_r"].conj().T
    is_block_diagonal = model_parameters_dict["zeta_matrix_u_r"][1,1] == model_parameters_dict["zeta_matrix_u_r"][0,0]

    if not is_hermitian.all():
        raise Exception("zeta_matrix_u_r is not hermitian")
    elif not is_block_diagonal:
        raise Exception("zeta_matrix_u_r is not block diagonal")
    
    # pass zeta_matrix_d_r to params_dict

    params_dict["ZETARD33"] = model_parameters_dict["zeta_matrix_d_r"][2,2]
    params_dict["ZETARDLL"] = model_parameters_dict["zeta_matrix_d_r"][1,1]
    
    is_hermitian =  model_parameters_dict["zeta_matrix_d_r"] == model_parameters_dict["zeta_matrix_d_r"].conj().T
    is_block_diagonal = model_parameters_dict["zeta_matrix_d_r"][1,1] == model_parameters_dict["zeta_matrix_d_r"][0,0]

    if not is_hermitian.all():
        raise Exception("zeta_matrix_d_r is not hermitian")
    elif not is_block_diagonal:
        raise Exception("zeta_matrix_d_r is not block diagonal")

    # pass kappau to params_dict
    params_dict["KAPPAU"] = model_parameters_dict["kappau"]
    params_dict["KAPPAUTILDE"] = model_parameters_dict["kappautilde"]

    # pass kappazp to params_dict
    params_dict["KAPPAZP"] = model_parameters_dict["kappazp"]
    return params_dict