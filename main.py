###
### Optimise roadmap based on client growth or arr growth
###

from functions import *
from settings import *

def main(df_ref):
    ###
    ### SETTINGS
    ###
    # print('\n', get_time(settings.time0), 'SETTINGS:', '\n')
    # print(get_time(settings.time0), 'Filter on SEGMENT: ', str(OPTIMISATION_SEGMENT), ' users')
    # print(get_time(settings.time0), 'Total clients in segment: ', str(len(df_ref[(df_ref['subscription_quantity'] >= OPTIMISATION_SEGMENT[0])
    #                                                                        & (df_ref['subscription_quantity'] <= OPTIMISATION_SEGMENT[1])])))
    # print(get_time(settings.time0), 'Total ARR in segment: ', str(df_ref[(df_ref['subscription_quantity'] >= OPTIMISATION_SEGMENT[0])
    #                                                                & (df_ref['subscription_quantity'] <= OPTIMISATION_SEGMENT[1])].arr.sum()))
    # print(get_time(settings.time0), 'Max roadmap items:', ROADMAP_LENGTH)
    # print(get_time(settings.time0), 'Fixed roadmap start:', ROADMAP_START,'\n')

    ###
    ### DATA PREPARATION
    ###
    # df = df_ref[(df_ref['subscription_quantity'] >= OPTIMISATION_SEGMENT[0]) & (df_ref['subscription_quantity'] <= OPTIMISATION_SEGMENT[1])]
    df = df_ref
    df_apps = analyse_apps(df)
    print('\n', get_time(settings.time0), df_apps, '\n')
    ###
    ### ENTER ROADMAP
    ###
    roadmap_sequence_input = input("Please enter the roadmap by prioriting the indices, eg 0,1,7,2,4,3,5,14,22,12,10,26,8: \n")
    roadmap_sequence = [int(s) for s in roadmap_sequence_input.split(',')]
    roadmap = create_roadmap(roadmap_sequence, df_apps)
    print('\n', get_time(settings.time0), f'You entered {roadmap_sequence}', ' resulting in:', roadmap, '\n')

    min_users_input = 2

    time.sleep(3)
    print('\n', get_time(settings.time0), 'Roadmap to be analysed: ', roadmap, '\n')

    ###
    ### RETRIEVE LIST OF CLIENTS PER ROADMAP ITEM
    ###
    #loop over roadmap per progressing roadmap item
    dfs_results = list()
    roadmaps = list()
    i = 0
    while i < len(roadmap):
        roadmap_i = roadmap[0:i+1]
        # Get all App columns except those in the roadmap
        apps_not_in_roadmap = [col for col in df if (col.startswith('App.') and not col in roadmap_i)]
        # Remove client when he uses an app which is not in roadmap
        df_i = df[~df[apps_not_in_roadmap].eq(1).any(1)]
        roadmaps.append(roadmap_i)
        dfs_results.append(df_i)
        i = i+1

    pd.set_option('display.max_rows', None)
    # Create a Pandas Excel writer using XlsxWriter as the engine.
    # writer = pd.ExcelWriter('clients_per_roadmap_item.xlsx', engine='openpyxl')
    for j, r in enumerate(roadmaps):
        print('\n', get_time(settings.time0), 'Roadmap so far...: ', r)
        # print('\n', get_time(settings.time0), 'Corresponding Dataframe: ', '\n', dfs_results[j], '\n')
        if j==0:
            print('\n', get_time(settings.time0), 'Client transfer list: ', '\n', dfs_results[j][dfs_results[j].subscription_quantity >= min_users_input][['name','subscription_quantity','arr']], '\n')
        else:
            print('\n', get_time(settings.time0), 'Client transfer list (in addition to previous): ', '\n', pd.concat([dfs_results[j],dfs_results[j-1]]).drop_duplicates(keep=False)
            [dfs_results[j].subscription_quantity >= min_users_input][['name','subscription_quantity','arr']], '\n')
        # dfs_results[j].to_excel(writer, sheet_name=str(r))
    # Close the Pandas Excel writer and output the Excel file.
    # writer.save()

    print('\n', get_time(settings.time0), 'Total duration of main: ', get_time(settings.time00), '\n')

    ### POST-OPERATIONS:
    # dfs_results[1][dfs_results[1].subscription_quantity > 40][['name','subscription_quantity','arr']]

    return None

if __name__ == "__main__":
    df_ref = data_prep(DATA)
    main(df_ref)

###  
