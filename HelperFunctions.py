from mlrose_hiive import SARunner as sa
from mlrose_hiive import GARunner as ga
from mlrose_hiive import RHCRunner as rhc
from mlrose_hiive import MIMICRunner as mimic
import mlrose_hiive
from time import time

def run_rh(problem, params):
    start = time()
    rh = rhc(problem           = problem, 
             experiment_name   = 'RHExperiment', 
             restart_list      = [100],
             **params)

    rhc_run_stats, rhc_run_curves = rh.run()
    rh_time = time() - start
    return rhc_run_stats, rhc_run_curves, rh_time


def run_sa(problem, params):
    start = time()
    sa_alg = sa(problem, 
                experiment_name   = "SAExperiment", 
                temperature_list  = [1, 10, 50, 100, 250],
                decay_list        = [mlrose_hiive.ExpDecay,mlrose_hiive.GeomDecay],
                **params)

    sa_run_stats, sa_run_curves = sa_alg.run()
    sa_time = time() - start
    return sa_run_stats, sa_run_curves, sa_time

def run_ga(problem, params):
    start = time()

    ga_alg = ga(problem          = problem,
                experiment_name  = "GAExperiment",
                population_sizes = [20,50,100],
                mutation_rates   = [0.1, 0.25, 0.5],
                **params)
    ga_run_stats, ga_run_curves = ga_alg.run()   
    ga_time = time() - start
    return ga_run_stats, ga_run_curves, ga_time

def run_mimic(problem, params):
    start = time()

    mmc = mimic(problem            = problem,
                experiment_name    = "MIMICExperiment",
                population_sizes   = [50, 100, 200, 250],
                keep_percent_list  = [.1, 0.25, 0.5, 0.75],
                use_fast_mimic     = True,
                **params)

    # the two data frames will contain the results
    mmc_run_stats, mmc_run_curves = mmc.run()

    mimic_time = time() - start
    return mmc_run_stats, mmc_run_curves, mimic_time