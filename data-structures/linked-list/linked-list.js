"use strict"

class element {
	constructor(data) {
		this.data = data;
		this.right = null;
		this.left = null;
	}
}

class linkedList {
	constructor (...elts) {
		this.head = elts[0]
		this.tail = elts.at(-1);
		this.length = 0;
	}

	getHead() { return this.head }

	getTail() { return this.tail }

	size() { return this.length }

	isTail(elt) {return (elt === this.tail) }

	fromArray(arr) {}

	destroy() {}

	find(elt) {
		//finds the first occurrence of elt
		let cur = this.getHead();
		while (cur) {
			if (cur.data === elt) return cur
			cur = cur.right;
		}
		return -1;
	}
	printAll() {
		let cur = this.getHead();
		while (cur) {
			console.log(`data: ${cur.data}, left: ${(cur.left == null) ? null : cur.left.data}, right: ${(cur.right == null) ? null : cur.right.data}`)
			cur = cur.right;
		}
		console.log("===================================");
		console.log(`head: ${this.head.data}, tail: ${this.tail.data}, length: ${this.length}\n`);
	}
}

class singleLinkedList extends linkedList {
	constructor(...elts) {
		super(...elts)
		this.length = elts.length;
		let cur = new element(elts[0])
		this.head = cur;
		for (let i = 1; i < elts.length; i++) {
			let elt = new element(elts[i]);
			cur.right = elt;
			cur = elt;
		}	
		this.tail = cur;
	}

	has(elt) {
		if (this.find(elt)) return true;
		return false;
	}

	print() {
		let cur = this.getHead();
		let str = ""
		while (cur) {
			str += cur.data.toString() + " ";
			cur = cur.right;
		}
		console.log(str);
		console.log("===================================");
	}

	insertRight(elt) {
		if (! elt instanceof element) return -1
		this.tail.right = elt;
		this.tail = elt;
		this.length++;
		return 0
	}

	remove(elt) {
		// removes first occurrence of elt
		
		// checks if its head or tail
		if (elt === this.getHead().data) {
			this.length--;
			this.head = this.head.right;
			return 0;
		}

		// traverse to find element and next
		let cur = this.getHead();
		let next = cur.right;
		let f = false;

		while (cur) {
			if (!next) break;
			if (next.data === elt) {
				f = true
				break;
			}
			cur = cur.right;
			next = cur.right;
		}
		if (!f) return -1;

		// if last pointer === null than elt == tail.data
		if (!next) {
			this.tail = cur;
			cur.right = null;
		} else
			// switch cur right ptr
			cur.right = next.right;

		// update length
		this.length--;

		return 0;
	}
}

class doubleLinkedList extends linkedList {
	constructor(...elts) {
		super(...elts)
		this.length = elts.length;
		let cur = new element(elts[0]);
		this.head = cur;
		for (let i = 1; i < elts.length; i++) {
			let elt = new element(elts[i])
			cur.right = (i <= elts.length - 1) ? elt : null;
			elt.left = (i >= 1) ? cur : null;
			cur = elt;
		}	
		this.tail = cur
	}

	print(dir="l") {
		let str = "";
		let cur;
		switch (dir) {
			case 'l':
				cur = this.getHead();
				while (cur) {
					str += cur.data.toString() + ' ';
					cur = cur.right;
				}
				break;
			case 'r':
				cur = this.getTail();
				while (cur) {
					str += cur.data.toString() + ' ';
					cur = cur.left;
				}
				break;
		}
		console.log(str);
	}

	insertAfter(e, n) {
		let cur = this.find(n)
		if (cur === -1) return -1;
		let elt = new element(e)

		elt.right = cur.right;
		elt.left = cur;

		if (cur.right) cur.right.left = elt;
		else this.tail = elt;
		cur.right = elt;

		this.length++;
	}

	insertBefore(e, cur) {
		if (cur === -1) {
			console.log("err");
			return -1;
		}
		let elt = new element(e)

		// set pointers
		elt.left = cur.left;
		elt.right = cur;

		if (cur.left) cur.left.right = elt;
		else this.head = elt
		cur.left = elt;
		
		this.length++;
	}

	removeAfter(n) {
		// removers element after n
		let cur = this.find(n)

		if (!cur.right) return -1;
		const link = cur.right.right;
		if (link) link.left = cur;
		else this.tail = cur;
		cur.right = link;
		this.length--;
	}

	removeBefore(n) {
		// removes element before n
		let cur = this.find(n)

		if (!cur.left) return -1
		const link = cur.left.left;
		if (link) link.right = cur
		else this.head = cur;
		cur.left = link
		this.length--;
	}

	remove(e) {
		// remove first instance of elements with data == e
		let cur = this.find(e);
		if (cur === -1) return -1
		if (cur.left != null) cur.left.right = cur.right
		else this.head = cur.right;
		if (cur.right != null) cur.right.left = cur.left
		else this.tail = cur.left;
		this.length--;
	}
}

class cycleLinkedList {
	constructor(...elts) {
		this.length = elts.length;

		let cur = new element(elts[0]);
		this.head = cur
		for (let i = 1; i < elts.length; i++) {
			let elt = new element(elts[i])

			cur.right = (i <= elts.length - 1) ? elt : this.head
			elt.left = (i >= 1) ? cur : null;
			cur = elt;
		}
		cur.right = this.head;
		this.head.left = cur;
		this.head = cur;
	}

	printAll(limit=0) {
		if (!this.head) {
			console.log(`head: ${this.head}, length: ${this.length}\n`);
			return -1
		}
		let cur = this.head; 
		limit *= this.length;
		let c = 0;
		while (cur.right != this.head || c < limit) {
			console.log(`data: ${cur.data}, left: ${(cur.left == null) ? null : cur.left.data}, right: ${(cur.right == null) ? null : cur.right.data}`)
			cur = cur.right;
			c++;
		}
		console.log("===================================");
		console.log(`head: ${this.head.data}, length: ${this.length}\n`);
	}

	kill() {
		this.head = null;
		this.length = 0;
	}

	// macros
	size() { return this.length }
	getHead() { return this.head }
	data(node) { return node.data }
	next(node) { return node.right }
	prev(node) { return node.left }
}


function main() {
	const tests = [
		11, 12, 13, 14,
		15, 16, 17, 18,
	];
	const slist = new singleLinkedList(...tests);
	const dlist = new doubleLinkedList(...tests);
	const clist = new cycleLinkedList(...tests);

}
main();

