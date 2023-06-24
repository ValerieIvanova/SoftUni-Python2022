// function sprintReview(input) {
//     const n = Number(input.shift());
//     const sprintBoardState = {};
//     let commandsDict = {
//         'Add New': addNew,
//         'Change Status': changeStatus,
//         'Remove Task': removeTask
//     };
//
//     for (let i = 0; i < n; i++) {
//         let [assignee, taskId, title, status, estimatedPoints] = input[i].split(':');
//         if (!sprintBoardState[assignee]) {
//             sprintBoardState[assignee] = [];
//         }
//         sprintBoardState[assignee].push({taskId, title, status, estimatedPoints: Number(estimatedPoints)});
//     }
//
//     for (let i = n; i < input.length; i++) {
//         let info = input[i].split(':');
//         let command = info.shift();
//         commandsDict[command](...info);
//     }
//
//     function addNew(assignee, taskId, title, status, estimatedPoints) {
//         if (!sprintBoardState[assignee]) {
//             console.log(`Assignee ${assignee} does not exist on the board!`);
//         } else {
//             sprintBoardState[assignee].push({taskId, title, status, estimatedPoints: Number(estimatedPoints)});
//         }
//     }
//
//     function changeStatus(assignee, taskId, newStatus) {
//         if (!sprintBoardState[assignee]) {
//             console.log(`Assignee ${assignee} does not exist on the board!`);
//         } else if (!sprintBoardState[assignee].taskId === taskId) {
//             console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
//         } else {
//             let taskIndex = sprintBoardState[assignee].findIndex(task => task.taskId === taskId);
//             sprintBoardState[assignee][taskIndex].status = newStatus;
//         }
//     }
//
//     function removeTask(assignee, index) {
//         let indexNum = Number(index);
//         if (!sprintBoardState[assignee]) {
//             console.log(`Assignee ${assignee} does not exist on the board!`);
//         } else if (indexNum < 0 || indexNum >= sprintBoardState[assignee].length) {
//             console.log('Index is out of range!');
//         }
//
//     }
// }
//
// sprintReview([
//         '5',
//         'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
//         'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
//         'Peter:BOP-1211:POC:Code Review:5',
//         'Georgi:BOP-1212:Investigation Task:Done:2',
//         'Mariya:BOP-1213:New Account Page:In Progress:13',
//         'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
//         'Change Status:Peter:BOP-1290:ToDo',
//         'Remove Task:Mariya:1',
//         'Remove Task:Joro:1',
//     ]
// );


function sprintReview(input) {
    const n = Number(input.shift());
    const sprintBoardState = {};
    let commandsDict = {
        'Add New': addNew,
        'Change Status': changeStatus,
        'Remove Task': removeTask
    };

    for (let i = 0; i < n; i++) {
        let [assignee, taskId, title, status, estimatedPoints] = input[i].split(':');
        if (!sprintBoardState[assignee]) {
            sprintBoardState[assignee] = [];
        }
        sprintBoardState[assignee].push({taskId, title, status, estimatedPoints: Number(estimatedPoints)});
    }

    for (let i = n; i < input.length; i++) {
        let info = input[i].split(':');
        let command = info.shift();
        commandsDict[command](...info);
    }

    function addNew(assignee, taskId, title, status, estimatedPoints) {
        if (!sprintBoardState[assignee]) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
            sprintBoardState[assignee].push({taskId, title, status, estimatedPoints: Number(estimatedPoints)});
        }
    }

    function changeStatus(assignee, taskId, newStatus) {
        if (!sprintBoardState[assignee]) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
        } else {
            let task = sprintBoardState[assignee].find(task => task.taskId === taskId);
            if (!task) {
                console.log(`Task with ID ${taskId} does not exist for ${assignee}!`);
            } else {
                task.status = newStatus;
            }
        }
    }

    function removeTask(assignee, index) {
        let indexNum = Number(index);
        if (!sprintBoardState[assignee]) {
            console.log(`Assignee ${assignee} does not exist on the board!`);
        } else if (indexNum < 0 || indexNum >= sprintBoardState[assignee].length) {
            console.log('Index is out of range!');
        } else {
            sprintBoardState[assignee].splice(indexNum, 1);
        }
    }


    let toDoPts = 0;
    let inProgressPts = 0;
    let codeReviewPts = 0;
    let donePoints = 0;

    for (let assignee in sprintBoardState) {
        sprintBoardState[assignee].forEach(task => {
            switch (task.status) {
                case 'ToDo':
                    toDoPts += task.estimatedPoints;
                    break;
                case 'In Progress':
                    inProgressPts += task.estimatedPoints;
                    break;
                case 'Code Review':
                    codeReviewPts += task.estimatedPoints;
                    break;
                case 'Done':
                    donePoints += task.estimatedPoints;
                    break;
                default:
                    break;
            }
        });
    }

    console.log(`ToDo: ${toDoPts}pts`);
    console.log(`In Progress: ${inProgressPts}pts`);
    console.log(`Code Review: ${codeReviewPts}pts`);
    console.log(`Done Points: ${donePoints}pts`);

    if (donePoints >= toDoPts + inProgressPts + codeReviewPts) {
        console.log('Sprint was successful!');
    } else {
        console.log('Sprint was unsuccessful...');
    }
}

// sprintReview([
//         '5',
//         'Kiril:BOP-1209:Fix Minor Bug:ToDo:3',
//         'Mariya:BOP-1210:Fix Major Bug:In Progress:3',
//         'Peter:BOP-1211:POC:Code Review:5',
//         'Georgi:BOP-1212:Investigation Task:Done:2',
//         'Mariya:BOP-1213:New Account Page:In Progress:13',
//         'Add New:Kiril:BOP-1217:Add Info Page:In Progress:5',
//         'Change Status:Peter:BOP-1290:ToDo',
//         'Remove Task:Mariya:1',
//         'Remove Task:Joro:1',
//     ]
// );

sprintReview(  [
        '4',
        'Kiril:BOP-1213:Fix Typo:Done:1',
        'Peter:BOP-1214:New Products Page:In Progress:2',
        'Mariya:BOP-1215:Setup Routing:ToDo:8',
        'Georgi:BOP-1216:Add Business Card:Code Review:3',
        'Add New:Sam:BOP-1237:Testing Home Page:Done:3',
        'Change Status:Georgi:BOP-1216:Done',
        'Change Status:Will:BOP-1212:In Progress',
        'Remove Task:Georgi:3',
        'Change Status:Mariya:BOP-1215:Done',
    ]
)