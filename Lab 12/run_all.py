"""Run all five Week 12 tasks, in order, with one command."""
import task_01_dataset_exploration as task1
import task_02_entropy_information_gain as task2
import task_03_train_decision_tree as task3
import task_04_evaluation_visualization as task4
import task_05_predict_sample as task5

def main():
    for task in [task1, task2, task3, task4, task5]:
        task.run()
    print("\nAll 5 Week 12 tasks completed successfully!")
    print("Open the outputs/ folder for graphs, predictions, metrics and explanations.")

if __name__ == "__main__":
    main()
